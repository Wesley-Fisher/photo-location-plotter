import os

class Helper:
    def __init__(self):
        pass
    
    def get_app_dir(self):
        return os.path.dirname(os.path.realpath(__file__)) + "/../"