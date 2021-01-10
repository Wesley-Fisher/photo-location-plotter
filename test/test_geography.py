import unittest
import logging

from photo_location_plotter.geography import *

from .helper import Helper
helper = Helper()

class TestRange(unittest.TestCase):

    def test_inside(self):
        r = Range(0, 10)
        self.assertTrue(r.contains(5))

    def test_less(self):
        r = Range(0, 10)
        self.assertFalse(r.contains(-1))

    def test_min(self):
        r = Range(0, 10)
        self.assertTrue(r.contains(0))

    def test_greater(self):
        r = Range(0, 10)
        self.assertFalse(r.contains(11))

    def test_max(self):
        r = Range(0, 10)
        self.assertTrue(r.contains(10))


class TestSimpleGeographyRegion(unittest.TestCase):
    '''
    1| 2 |3
    4|(5)|6
    7| 8 |9
    '''

    def get_default_region(self):
        return SimpleGeographyRegion(Range(-5, 5), Range(-5, 5))

    def test_zone_1(self):
        self.assertFalse(self.get_default_region().contains(-6, 6))

    def test_zone_2(self):
        self.assertFalse(self.get_default_region().contains(0, 6))

    def test_zone_3(self):
        self.assertFalse(self.get_default_region().contains(6, 6))

    def test_zone_4(self):
        self.assertFalse(self.get_default_region().contains(-6, 0))

    def test_zone_5(self):  
        self.assertTrue(self.get_default_region().contains(0, 0))

    def test_zone_6(self):
        self.assertFalse(self.get_default_region().contains(6, 0))

    def test_zone_7(self):
        self.assertFalse(self.get_default_region().contains(-6, -6))

    def test_zone_8(self):
        self.assertFalse(self.get_default_region().contains(0, -6))

    def test_zone_9(self):
        self.assertFalse(self.get_default_region().contains(6, -6))


class TestGeographyRegion(unittest.TestCase):

    def test_constructor(self):
        r = GeographyRegion(-2, 2,-2, 2)
        self.assertEqual(len(r.regions), 1)

    def test_simple_region(self):
        r = GeographyRegion.from_dict({'longitude': [-2, 2], 'latitude': [-2, 2]})
        self.assertEqual(len(r.regions), 1)

    def test_simple_region(self):
        r = GeographyRegion.from_dict({'longitude': [187, -187], 'latitude': [-2, 2]})
        self.assertEqual(len(r.regions), 2)