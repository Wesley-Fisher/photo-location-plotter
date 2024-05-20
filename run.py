#!/usr/bin/python3

import sys
import os
import yaml

import photo_location_plotter.settings as Settings
import photo_location_plotter.application as APP

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Call with config file as argument")
        exit()

    config_file = sys.argv[1]
    if not os.path.isfile(config_file):
        print(f"Could not find file [{config_file}]")
        exit()

    with open(config_file) as handle:
        try:
            settings = yaml.safe_load(handle)
        except Exception as e:
            print(e)
            exit()
    
    for project in settings['projects']:
        print(project['name'])
        
        app = APP.Application(config_file, project)
        app.run()