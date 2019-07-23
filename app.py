from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():

    print("request:")
    print(request.headers)

    print("path:")
    print(request.path)

    print("args:")
    print(request.args)

    return "aaaa"
    
@app.route('/shi')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
