import os
import logging

import exifread as ef

from .geography import Point

class GPSExtractor:
    def __init__(self, logger):
        self.logger = logger
        logging.getLogger(ef.__name__).setLevel(logging.WARNING)

        self.LAT_KEY = 'GPS GPSLatitude'
        self.LAT_REF_KEY = 'GPS GPSLatitudeRef'
        self.LON_KEY = 'GPS GPSLongitude'
        self.LON_REF_KEY = 'GPS GPSLongitudeRef'

    def get_file_info(self, filename):
        if '.jpg' in filename:
            return self.get_file_info_exifread(filename)
        if '.mp4' in filename:
            return self.get_file_info_exifread(filename)
        return {}

    def get_file_info_exifread(self, filename):
        tags = {}
        with open(filename, 'rb') as f:
            tags = ef.process_file(f, details=False)
        return tags

    def to_degrees(self, value):
        # borrowed from: https://gist.github.com/snakeye/fdc372dbf11370fe29eb
        #                https://stackoverflow.com/questions/19804768/interpreting-gps-info-of-exif-data-from-photo-in-python
        d = float(value.values[0].num) / float(value.values[0].den)
        m = float(value.values[1].num) / float(value.values[1].den)
        s = float(value.values[2].num) / float(value.values[2].den)

        return d + (m / 60.0) + (s / 3600.0)

    def get_latlon_value(self, tags, key, ref_key, flip_ref_val):
        val = tags.get(key)
        if val:
            val = self.to_degrees(val)
            if str(tags.get(ref_key)) == flip_ref_val:
                val = -val
        else:
            return None
        return float(val)


    def get_gps(self, filename):
        tags = self.get_file_info(filename)

        lat = self.get_latlon_value(tags, self.LAT_KEY, self.LAT_REF_KEY, 'S')
        lon = self.get_latlon_value(tags, self.LON_KEY, self.LON_REF_KEY, 'W')

        if lat is None or lon is None:
            self.logger.info('%s: No Info', filename)
            return None
        
        return Point(lat, lon)