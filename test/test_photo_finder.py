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
