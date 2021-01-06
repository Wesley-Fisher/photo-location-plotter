import unittest
import logging

from photo_location_plotter.photo_finder import PhotoFinder

from .helper import Helper
helper = Helper()

class TestPhotoFinder(unittest.TestCase):

    def test_extracts_all_files(self):
        pf = PhotoFinder(helper.get_test_ConfigSettings(),
                         helper.get_test_FileSystemHelper(),
                         helper.logger())
        self.assertEqual(len(pf.get_all_files()), 21)

    def test_absolute_directory(self):
        conf = helper.get_test_ConfigSettings()
        abs_dir = helper.get_app_dir() + "/projects/test_project/photos/subfolder_a"
        conf.config['photo_directories'] = [abs_dir]
        pf = PhotoFinder(conf,
                         helper.get_test_FileSystemHelper(),
                         helper.logger())
        self.assertEqual(len(pf.get_all_files()), 8)

    def test_relative_directory(self):
        conf = helper.get_test_ConfigSettings()
        rel_dir = '$PROJECT/photos/subfolder_b'
        conf.config['photo_directories'] = [rel_dir]
        pf = PhotoFinder(conf,
                         helper.get_test_FileSystemHelper(),
                         helper.logger())
        self.assertEqual(len(pf.get_all_files()), 6)
