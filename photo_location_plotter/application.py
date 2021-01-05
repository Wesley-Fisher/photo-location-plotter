
from .file_structure_helper import FileStructureHelper
from .settings import ConfigSettings
import yaml

class Application:
    def __init__(self, run_settings):
        self.run_settings = run_settings

    def run(self):
        file_system = FileStructureHelper(self.run_settings)

        config_settings = ConfigSettings(yaml.load(file_system.get_config_file_path(), Loader=yaml.SafeLoader))