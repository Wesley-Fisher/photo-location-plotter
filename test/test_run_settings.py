import unittest

from photo_location_plotter.run_settings import RunSettings

class TestRunSettings(unittest.TestCase):

    def test_extracts_project(self):
        proj = 'theproject'
        rs = RunSettings(['test_run_settings.py', proj])
        self.assertEqual(rs.project, proj)
    
    def test_fails_if_project_empty(self):
        try:
            rs = RunSettings(['test_run_settings.py'])
        except ValueError:
            self.assertTrue(True)
            return
        self.assertTrue(False)