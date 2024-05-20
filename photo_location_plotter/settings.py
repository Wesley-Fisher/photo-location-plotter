#!/usr/bin/python3

class ConfigSettings:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger


    def validate(self):
        keys = self.config.keys()

        if 'photo_directories' not in keys:
            raise KeyError("'photo_directories' not found in config file")
        
        pd = self.config['photo_directories']
        if pd is None or len(pd) == 0:
            raise KeyError("No photo_directories found")
