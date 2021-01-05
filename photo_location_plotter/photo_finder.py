
class PhotoFinder:
    def __init__(self, config, file_system_helper):
        self.config = config
        self.file_system_helper = file_system_helper
        self.file_types = ['.jpg', '.JPG', '.mp4']

    def get_files_list(self):
        pass