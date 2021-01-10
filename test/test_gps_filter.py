import unittest
import logging

from photo_location_plotter.geography import *
from photo_location_plotter.gps_filter import GPSFilter

from .helper import Helper
helper = Helper()


empty = {}

incl_1 = \
{'include_regions':
    [
        {'latitude': [-10, 10], 'longitude': [-10, 10]}
    ]
}

excl_1 = \
{'exclude_regions':
    [
        {'latitude': [-10, 10], 'longitude': [-10, 10]}
    ]
}

composite = \
{'include_regions':
    [
        {'latitude': [-10, 10], 'longitude': [0, 10]}
    ],
'exclude_regions':
    [
        {'latitude': [-10, 10], 'longitude': [5, 15]}
    ]
}


class TestGPSFilter(unittest.TestCase):

    def test_empty(self):
        filt = GPSFilter(empty, helper.logger)
        self.assertTrue(filt.point_passes(Point(0, 0)))

    def test_incl_included(self):
        filt = GPSFilter(incl_1, helper.logger)
        self.assertTrue(filt.point_passes(Point(0, 0)))

    def test_incl_excluded(self):
        filt = GPSFilter(incl_1, helper.logger)
        self.assertFalse(filt.point_passes(Point(20, 20)))


    def test_excl_inside(self):
        filt = GPSFilter(excl_1, helper.logger)
        self.assertFalse(filt.point_passes(Point(0, 0)))

    def test_excl_outside(self):
        filt = GPSFilter(excl_1, helper.logger)
        self.assertTrue(filt.point_passes(Point(20, 20)))

    
    def test_composite_outside_all(self):
        filt = GPSFilter(composite, helper.logger)
        self.assertFalse(filt.point_passes(Point(-30, -30)))

    def test_composite_excl_only(self):
        filt = GPSFilter(composite, helper.logger)
        self.assertFalse(filt.point_passes(Point(0, 13)))

    def test_composite_incl_only(self):
        filt = GPSFilter(composite, helper.logger)
        self.assertTrue(filt.point_passes(Point(3, 0)))

    def test_composite_both(self):
        filt = GPSFilter(composite, helper.logger)
        self.assertEqual(len(filt.include_regions), 1)
        self.assertEqual(len(filt.exclude_regions), 1)
        self.assertFalse(filt.point_passes(Point(0, 7)))