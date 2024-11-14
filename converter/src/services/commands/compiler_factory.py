from src.services.commands.java_command import JavaCommand
from src.services.commands.python_command import PythonCommand
from src.services.commands.command import Command

code_map = {
    'java': JavaCommand(),
    'python': PythonCommand()
}


class CompilerFactory:
    @staticmethod
    def get_instance(lang) -> Command:
        return code_map[lang]
