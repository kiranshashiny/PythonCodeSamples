from flask import Flask, render_template
app = Flask(__name__)

@app.route('/open/<float:open>')
def hello_name(open):
	return 'Stock open price  {}'.format(open)

@app.route('/welcome')
def welcome():
	return render_template('welcome.jg')

if __name__ == '__main__':
   app.run()
