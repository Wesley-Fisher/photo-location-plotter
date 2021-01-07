import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, logger):
        self.logger = logger

    def plot(self, config, file_system_helper, points):
        in_file = file_system_helper.get_project_directory() + "/" + config.config['map']['in_file']

        background = plt.imread(in_file)

        fig, ax = plt.subplots(figsize=(8,7))

        longs = [p.lon for p in points]
        lats = [p.lat for p in points]

        ax.scatter(longs, lats, zorder=1, alpha= 0.3, c='b', s=25)

        bounds = config.config['map']['bounds']
        ax.set_xlim(bounds['longitude'][0], bounds['longitude'][1])
        ax.set_ylim(bounds['latitude'][0], bounds['latitude'][1])

        BBox = (bounds['longitude'][0], bounds['longitude'][1], bounds['latitude'][0], bounds['latitude'][1])

        ax.imshow(background, zorder=0, extent=BBox, aspect='equal')
        out_file = file_system_helper.get_project_directory() + "/" + config.config['map']['out_file']
        plt.savefig(out_file, dpi=800)