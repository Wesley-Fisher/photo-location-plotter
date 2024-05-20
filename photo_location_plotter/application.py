import logging
import yaml

from .file_structure_helper import FileStructureHelper
from .settings import ConfigSettings
from .photo_finder import PhotoFinder
from .gps_extractor import GPSExtractor
from .plotter import Plotter
from .gps_filter import GPSFilter

class Application:
    def __init__(self, project_file, project_settings):
        self.project_directory = '/'.join(project_file.replace('\\', '/').split('/')[0:-1])
        self.project_name = project_settings['name']

        logging.basicConfig(format='%(levelname)s:  %(message)s',
                            filename= self.project_directory + "/log.txt",
                            filemode='w',
                            level=logging.DEBUG)
        self.logger = logging.getLogger("App")
        self.logger.info(project_file)
        self.logger.info("project: %s", project_settings['name'])
        self.settings = project_settings

    def log_points(self, points, filename):
        with open(filename, 'w') as file:
            file.write("LAT, LON\n")
            for pt in points:
                file.write("%f, %f\n" % (pt.lat, pt.lon))

    def run(self):
        config_contents = self.settings
        config_settings = ConfigSettings(config_contents, logger=self.logger.getChild("ConfigSettings"))
        config_settings.validate()

        photo_finder = PhotoFinder(config_settings, logger=self.logger.getChild("PhotoFinder"))
        files = photo_finder.get_all_files()

        points = []
        gps = GPSExtractor(logger=self.logger.getChild("GPSExtractor"))
        for filename in files:
            pt = gps.get_gps(filename)
            if pt is not None:
                points.append(pt)

        filt = GPSFilter(config_settings.config.get('regions', {}), self.logger.getChild("GPSFilter"))


        points, unused_points = filt.filter(points)

        self.log_points(points, self.project_directory + '/' + self.project_name + '_points_used.txt')
        self.log_points(unused_points, self.project_directory + '/' + self.project_name + '_points_unused.txt')
        

        plotter = Plotter(logger=self.logger.getChild("Plotter"))
        plotter.plot(config_settings, points)
