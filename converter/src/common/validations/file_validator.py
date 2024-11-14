import os
from src.common.validations.validator_strategy import ValidatorStrategy
from src.common.exceptions.parameter_exception import ParameterException


class FileValidator(ValidatorStrategy):
    def __init__(self, data, is_file):
        self.data = data
        self.is_file = is_file

    def validate(self):
        if self.is_file:
            is_file = os.path.isfile(self.data)
            if not is_file:
                raise ParameterException('Invalid file path')
        else:
            is_folder = os.path.isdir(self.data)
            if not is_folder:
                raise  ParameterException('Invalid folder path')
