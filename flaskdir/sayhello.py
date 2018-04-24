from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World’

if __name__ == '__main__':
   app.run()

@app.route('/sayhello/<name>')
def sayhello_name(name):
   return ‘Hello, My name is %s!' % name

