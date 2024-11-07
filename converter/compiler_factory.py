from java_command import JavaCommand
from python_command import PythonCommand
from command import Command

code_map = {
    'java': JavaCommand(),
    'python': PythonCommand()
}


class CompilerFactory:
    @staticmethod
    def get_instance(lang) -> Command:
        return code_map[lang]
