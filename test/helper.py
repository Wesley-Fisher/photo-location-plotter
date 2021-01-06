import os
import logging
import yaml

from photo_location_plotter.settings import RunSettings, ConfigSettings
from photo_location_plotter.file_structure_helper import FileStructureHelper

class Helper:
    def __init__(self):
        pass
    
    def get_app_dir(self):
        return os.path.dirname(os.path.realpath(__file__)) + "/../"

    def logger(self):
        return logging.getLogger("Testing")
    
    def get_test_RunSettings(self):
        return RunSettings(['test_project'], self.get_app_dir())
    
    def get_test_FileSystemHelper(self):
        return FileStructureHelper(self.get_test_RunSettings())

    def read_yaml(self, filepath):
        with open(filepath, 'r') as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as e:
                self.logger.exception(e)

    def get_test_ConfigSettings(self):
        filename = self.get_app_dir() + "/projects/test_project/config.yaml"
        conf = self.read_yaml(filename)
        return ConfigSettings(conf, self.logger())

