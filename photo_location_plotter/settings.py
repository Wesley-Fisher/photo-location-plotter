#!/usr/bin/python3

class RunSettings:
    def __init__(self, argv, app_directory):
        self.project = argv[-1]
        if '.py' in self.project:
            raise ValueError("No project given in RunSettings (expected via command line)")
        
        self.app_directory = app_directory

class ConfigSettings:
    def __init__(self, config):
        self.config = config

    def validate(self):
        keys = self.config.keys()

        if 'photos' not in keys:
            raise KeyError("'photos' not found in config file")