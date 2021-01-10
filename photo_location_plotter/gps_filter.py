
from .geography import GeographyRegion

class GPSFilter:
    def __init__(self, config, logger):
        self.logger = logger
        self.include_regions = [GeographyRegion.from_dict(data) for data in config.get('include_regions', [])]
        self.exclude_regions = [GeographyRegion.from_dict(data) for data in config.get('exclude_regions', [])]


    def filter(self, points):
        points_pass = []
        points_fail = []

        for point in points:
            if self.point_passes(point):
                points_pass.append(point)
            else:
                points_fail.append(point)

        return points_pass, points_fail
    
    def point_passes(self, point):
        
        if any([r.contains(point.lon, point.lat) for r in self.exclude_regions]):
            return False
        
        if len(self.include_regions) == 0:
            return True

        if any([r.contains(point.lon, point.lat) for r in self.include_regions]):
            return True

        return False