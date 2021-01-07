import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, logger):
        self.logger = logger

    def plot(self, config, file_system_helper, points):
        in_file = file_system_helper.get_project_directory() + "/" + config.config['map']['in_file']

        background = plt.imread(in_file)

        fig, ax = plt.subplots()
        fig.tight_layout(pad=0.0)

        longs = [p.lon for p in points]
        lats = [p.lat for p in points]

        styling = config.config.get('styling', {})

        ax.scatter(longs, lats, alpha=styling.get('point_alpha', 0.3), c=styling.get('point_color', 'b'), s=styling.get('point_size', 25))

        bounds = config.config['map']['bounds']
        ax.set_xlim(bounds['longitude'][0], bounds['longitude'][1])
        ax.set_ylim(bounds['latitude'][0], bounds['latitude'][1])
        BBox = (bounds['longitude'][0], bounds['longitude'][1], bounds['latitude'][0], bounds['latitude'][1])

        ax.set_xticklabels([])
        ax.set_xticks([])
        ax.set_yticklabels([])
        ax.set_yticks([])

        plt.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)

        ax.imshow(background, zorder=0, extent=BBox, aspect='equal')
        out_file = file_system_helper.get_project_directory() + "/" + config.config['map']['out_file']

        plt.savefig(out_file, dpi=800, bbox_inches='tight', pad_inches=0.1)