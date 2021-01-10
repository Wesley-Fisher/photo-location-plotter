
class GPSFilter:
    def __init__(self, config, logger):
        self.logger = logger

    def filter(self, points):
        points_pass = []
        points_fail = []

        for point in points:
            if self.point_passes(point)
                points_pass.append(point)
            else:
                points_fail.append(point)
    
    def point_passes(self, point):
        return True