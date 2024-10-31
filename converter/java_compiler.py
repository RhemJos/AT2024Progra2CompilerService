import subprocess
from pathlib import Path


class JavaCompiler:
    def compiler(self, java_file, java_folder):
        print('compiler 1')
        java_compiler = 'C:/"Program Files"/Java/jdk1.8.0_251/bin/javac '
        java_execute = 'C:/"Program Files"/Java/jdk1.8.0_251/bin/java'
        java_cp_param = ' -cp '
        java_and = ' && '
        file_name = Path(java_file).stem
        cmd = java_compiler + java_file + java_and + java_execute + java_cp_param + java_folder + ' ' + file_name
        return subprocess.check_output(cmd, shell=True)
