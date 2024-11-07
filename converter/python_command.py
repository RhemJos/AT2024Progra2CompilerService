from command import Command


class PythonCommand(Command):

    def __init__(self):
        self.name = "python"

    def build(self, parameter):
        python_compiler = parameter.get_binary() + 'python '
        cmd = python_compiler + parameter.get_file_path()
        return cmd
