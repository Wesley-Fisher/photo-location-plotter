import os

class PhotoFinder:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
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
        return [d for d in self.config.config['photo_directories']]
    
    def get_files_in_directory(self, directory):
        return [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames if os.path.splitext(f)[1] in self.file_types]
        