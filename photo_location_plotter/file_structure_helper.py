
class FileStructureHelper:
    def __init__(self, run_settings):
        self.run_settings = run_settings

    def get_project_directory(self):
        return self.run_settings.app_directory + '/projects/' + self.run_settings.project

    def get_config_file_path(self):
        return self.get_project_directory() + "/config.yaml"