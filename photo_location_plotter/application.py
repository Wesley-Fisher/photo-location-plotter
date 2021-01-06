import logging
import yaml

from .file_structure_helper import FileStructureHelper
from .settings import ConfigSettings
from .photo_finder import PhotoFinder

class Application:
    def __init__(self, run_settings):
        self.run_settings = run_settings
        self.file_system = FileStructureHelper(self.run_settings)

        logging.basicConfig(format='%(levelname)s:  %(message)s',
                            filename=self.file_system.get_project_directory()+"/log.txt",
                            filemode='w',
                            level=logging.DEBUG)
        self.logger = logging.getLogger("App")
        self.logger.info(self.file_system.get_project_directory())
        self.logger.info("project: %s", self.run_settings.project)

    def read_yaml(self, filepath):
        with open(filepath, 'r') as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as e:
                self.logger.exception(e)

    def run(self):
        config_contents = self.read_yaml(self.file_system.get_config_file_path())
        config_settings = ConfigSettings(config_contents, logger=self.logger.getChild("ConfigSettings"))
        config_settings.validate()

        photo_finder = PhotoFinder(config_settings, self.file_system, logger=self.logger.getChild("PhotoFinder"))
        files = photo_finder.get_all_files()
