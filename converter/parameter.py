class Parameter:

    def __init__(self, file_path, folder_path, binary_path):
        self.file_path = file_path
        self.folder_path = folder_path
        self.binary_path = binary_path

    def get_file_path(self):
        return self.file_path

    def get_folder_path(self):
        return self.folder_path

    def get_binary(self):
        return self.binary_path
