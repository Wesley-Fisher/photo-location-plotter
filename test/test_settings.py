import unittest

from photo_location_plotter.settings import RunSettings

class TestRunSettings(unittest.TestCase):

    def test_extracts_project(self):
        proj = 'theproject'
        rs = RunSettings(['test_run_settings.py', proj], 'app_dir')
        self.assertEqual(rs.project, proj)
    
    def test_fails_if_project_empty(self):
        try:
            rs = RunSettings(['test_run_settings.py'], 'app_dir')
        except ValueError:
            self.assertTrue(True)
            return
        self.assertTrue(False)

    def test_saves_app_directory(self):
        proj = 'theproject'
        direct = 'app_dir'
        rs = RunSettings(['test_run_settings.py', proj], direct)
        self.assertEqual(rs.app_directory, direct)