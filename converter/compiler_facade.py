from parameter import Parameter
from command import Command
from execute import Execute
from compiler_factory import CompilerFactory


class CompilerFacade:
    @staticmethod
    def compiler(lang, file, folder, binary):
        parameter = Parameter(file, folder, binary)
        command: Command = CompilerFactory.get_instance(lang)
        cmd = command.build(parameter)
        execute = Execute()
        return execute.run(cmd)
