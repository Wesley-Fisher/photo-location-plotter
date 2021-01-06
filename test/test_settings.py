import unittest
import logging

from photo_location_plotter.settings import RunSettings, ConfigSettings

from .helper import Helper
helper = Helper()

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


class TestConfigSettings(unittest.TestCase):

    def test_catches_no_directories(self):
        cs = ConfigSettings({}, helper.logger())
        try:
            cs.validate()
        except KeyError as e:
            return
        self.assertTrue(False)

    def test_catches_zero_directories(self):
        cs = ConfigSettings({'photo_directories': []}, helper.logger())
        try:
            cs.validate()
        except KeyError as e:
            return
        self.assertTrue(False)
