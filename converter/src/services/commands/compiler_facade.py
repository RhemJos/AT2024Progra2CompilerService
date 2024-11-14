from src.services.parameter import Parameter
from src.services.commands.command import Command
from src.services.execute import Execute
from src.services.commands.compiler_factory import CompilerFactory


class CompilerFacade:
    @staticmethod
    def compiler(lang, file, folder, binary):
        parameter = Parameter(file, folder, binary)
        command: Command = CompilerFactory.get_instance(lang)
        cmd = command.build(parameter)
        execute = Execute()
        return execute.run(cmd)
