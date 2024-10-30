from java_compiler import JavaCompiler
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    java_compiler = JavaCompiler()
    print(java_compiler.compiler())
