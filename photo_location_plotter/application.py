
from .file_structure_helper import FileStructureHelper


class Application:
    def __init__(self, run_settings):
        self.run_settings = run_settings

    def run(self):
        file_system = FileStructureHelper(self.run_settings)