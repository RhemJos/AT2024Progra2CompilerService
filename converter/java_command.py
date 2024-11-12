from pathlib import Path
from command import Command
from command_exception import CommandException


class JavaCommand(Command):

    def __init__(self):
        self.name = "java"

    def build(self, parameter):
        try:
            java_compiler = parameter.get_binary() + 'javac '
            java_execute = parameter.get_binary() + 'java'
            java_cp_param = ' -cp '
            java_and = ' && '
            file_name = Path(parameter.get_file_path()).stem
            cmd = java_compiler + parameter.get_file_path() + java_and + java_execute + java_cp_param + parameter.get_folder_path() + ' ' + file_name
            return cmd
        except Exception as error:
            raise CommandException("Java command error")
