import os
from java_compiler import JavaCompiler
from parameter import Parameter
from python_command import PythonCommand
from java_command import JavaCommand
from execute import Execute
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/compiler', methods=['POST'])
def route():
    java_file = request.files['file']
    lang = request.form.get('lang')
    folder_path ='D:/AT2024Progra/AT2024Progra2CompilerService/converter/upload/'
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, java_file.filename)
    java_file.save(file_path)

    cmd = ''
    if lang == 'java':
        parameter = Parameter(file_path, folder_path, 'C:/"Program Files"/Java/jdk1.8.0_251/bin/')
        java_command = JavaCommand()
        cmd = java_command.build(parameter)
        print(cmd)
    else:
        parameter = Parameter(file_path, folder_path, 'C:/python39/')
        python_command = PythonCommand()
        cmd = python_command.build(parameter)
        print(cmd)

    execute = Execute()
    return execute.run(cmd)

if __name__ == '__main__':
    app.run()
