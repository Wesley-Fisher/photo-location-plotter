import os
import logging

class Helper:
    def __init__(self):
        pass
    
    def get_app_dir(self):
        return os.path.dirname(os.path.realpath(__file__)) + "/../"

    def logger(self):
        return logging.getLogger("Testing")
    
