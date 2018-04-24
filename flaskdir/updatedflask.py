from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)
 
@app.route("/")
def index():
    return "Index!"
 
@app.route('/sayhello/<name>')
def sayhello_name(name):
    return ' Hello My name is %s '% name

 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
