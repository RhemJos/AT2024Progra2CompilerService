from pathlib import Path
from parameter_exception import ParameterException


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

    def validate(self):
        if self.file_path is None or self.folder_path is None or self.binary_path is None:
            raise ParameterException('Invalid Parameter')

        if not self.file_path or not self.folder_path or not self.binary_path:
            raise ParameterException('Parameters could not empty')

        file = Path(self.file_path)
        folder = Path(self.folder_path)
        folder_bin = Path(self.binary_path)
        if not file.is_file():
            raise ParameterException('file_path is not a file')
        if not folder.is_dir():
            raise ParameterException('folder_path is not a dir')
        if not folder_bin.is_dir():
            raise ParameterException('binary_path is not a dir')
