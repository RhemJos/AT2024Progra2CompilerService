import subprocess


class JavaCompiler:
    def compiler(self, java_file):
        cmd = 'C:/"Program Files"/Java/jdk1.8.0_251/bin/javac D:/AT2024Progra/EjemploJava7.java && C:/"Program Files"/Java/jdk1.8.0_251/bin/java -cp D:/AT2024Progra EjemploJava7'
        return subprocess.check_output(cmd, shell=True)
