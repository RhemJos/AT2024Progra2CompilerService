import unittest
from src.services.commands.java_command import JavaCommand
from src.services.parameter import Parameter
from src.common.exceptions.parameter_exception import ParameterException


class TestJavaCommand(unittest.TestCase):
    def test_build_success(self):
        parameter = Parameter('D:/AT2024Progra/EjemploJava7.java', 'D:/AT2024Progra/', 'D:/AT2024Progra/java/')
        command = JavaCommand()
        expected = 'D:/AT2024Progra/java/javac D:/AT2024Progra/EjemploJava7.java && D:/AT2024Progra/java/java -cp D:/AT2024Progra/ EjemploJava7'
        self.assertEqual(command.build(parameter), expected)

    def test_build_invalid_file(self):
        with self.assertRaises(ParameterException):
            parameter = Parameter(None, 'D:/AT2024Progra/', 'D:/AT2024Progra/java/')
            command = JavaCommand()
            command.build(parameter)
