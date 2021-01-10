
class Point:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

class Range:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def contains(self, val):
        return val >= self.min and val <= self.max


class SimpleGeographyRegion:
    def __init__(self, lon_range, lat_range):
        self.lon_range = lon_range
        self.lat_range = lat_range

    def contains(self, lon, lat):
        return self.lon_range.contains(lon) and self.lat_range.contains(lat)

class GeographyRegion:
    def __init__(self, lon_left, lon_right, lat_min, lat_max):
        self.regions = []

        lat_range = Range(lat_min, lat_max)

        if lon_left < lon_right:
            lon_range = Range(lon_left, lon_right)
            
            self.regions.append(SimpleGeographyRegion(lon_range, lat_range))
        else:

            lon_1 = Range(lon_left, 180.001)
            lon_2 = Range(-0.001, lon_right)
            self.regions.append(SimpleGeographyRegion(lon_1, lat_range))
            self.regions.append(SimpleGeographyRegion(lon_2, lat_range))
    
    def contains(self, lon, lat):
        return any(self.regions.contains(lon, lat))

    @staticmethod
    def from_dict(config):
        try:
            lon_0 = config['longitude'][0]
            lon_1 = config['longitude'][1]
            lat_0 = config['latitude'][0]
            lat_1 = config['latitude'][1]
            return GeographyRegion(lon_0, lon_1, lat_0, lat_1)
        except KeyError as e:
            raise e