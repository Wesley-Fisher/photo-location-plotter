import unittest

from photo_location_plotter.run_settings import RunSettings
from photo_location_plotter.file_structure_helper import FileStructureHelper

class TestFileStructureHelper(unittest.TestCase):

    def get_run_settings(self):
        return RunSettings(['test_file_structure_helper.py', 'test_project'], 'start_dir')

    def test_get_app_directory(self):
        fsh = FileStructureHelper(self.get_run_settings())
        self.assertEqual(fsh.get_project_directory(), 'start_dir/projects/test_project')
    
    def test_get_config_file_path(self):
        fsh = FileStructureHelper(self.get_run_settings())
        self.assertEqual(fsh.get_config_file_path(), 'start_dir/projects/test_project/config.yaml')