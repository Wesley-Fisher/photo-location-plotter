#!/usr/bin/python3

import sys
import os

import photo_location_plotter.run_settings as RS
import photo_location_plotter.application as APP

if __name__ == '__main__':
    run_settings = RS.RunSettings(argv=sys.argv, app_directory=os.path.dirname(os.path.realpath(__file__)))

    app = APP.Application(run_settings)
    app.run()