from pathlib import Path
from src.common.exceptions.parameter_exception import ParameterException
from src.common.validations.empty_or_none_validator import EmptyOrNoneValidator
from src.common.validations.file_validator import FileValidator
from src.common.validations.context import Context


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
        strategies = [
            EmptyOrNoneValidator('file_path', self.file_path),
            EmptyOrNoneValidator('folder_path', self.folder_path),
            EmptyOrNoneValidator('binary_path', self.binary_path),
            FileValidator(self.file_path, True),
            FileValidator(self.folder_path, False),
            FileValidator(self.binary_path, False)
        ]
        context = Context(strategies)
        context.validate()

