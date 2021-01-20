import os

class PhotoFinder:
    def __init__(self, config, file_system_helper, logger):
        self.config = config
        self.logger = logger
        self.file_system_helper = file_system_helper
        self.file_types = ['.jpg', '.JPG', '.mp4', '.MP4']

    def get_all_files(self):
        directories = self.get_directories()
        files = []
        self.logger.info("Directories")
        for d in directories:
            d_files = self.get_files_in_directory(d)
            files = files + d_files
            self.logger.info("  %s; found %d files", d, len(d_files))
        
        return files

    def get_directories(self):
        return [self.format_photo_directory(d) for d in self.config.config['photo_directories']]
    
    def format_photo_directory(self, d):
        if '$PROJECT' in d:
            return d.replace('$PROJECT', self.file_system_helper.get_project_directory())
        else:
            return d

    def get_files_in_directory(self, directory):
        return [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames if os.path.splitext(f)[1] in self.file_types]
        