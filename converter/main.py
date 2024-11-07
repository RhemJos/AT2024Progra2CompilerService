import os
from compiler_facade import CompilerFacade
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/compiler', methods=['POST'])
def route():
    file = request.files['file']
    lang = request.form.get('lang')
    folder_path ='D:/AT2024Progra/AT2024Progra2CompilerService/converter/upload/'
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file.filename)
    file.save(file_path)

    if lang == 'java':
        binary_path = 'C:/"Program Files"/Java/jdk1.8.0_251/bin/'
    else:
        binary_path ='C:/python39/'

    return CompilerFacade.compiler(lang, file_path, folder_path, binary_path)


if __name__ == '__main__':
    app.run()
