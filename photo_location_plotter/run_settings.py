#!/usr/bin/python3

class RunSettings:
    def __init__(self, argv):
        self.project = argv[-1]
        if '.py' in self.project:
            raise ValueError("No project given in RunSettings (expected via command line)")