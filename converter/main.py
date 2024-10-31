import os
from java_compiler import JavaCompiler

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/compiler', methods=['POST'])
def route():
    java_file = request.files['file']
    folder_path ='D:/AT2024Progra/AT2024Progra2CompilerService/converter/upload/'
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, java_file.filename)
    java_file.save(file_path)
    java_compiler = JavaCompiler()
    return java_compiler.compiler(file_path, folder_path)


if __name__ == '__main__':
    app.run()
    