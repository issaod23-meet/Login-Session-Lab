from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST'] ) # What methods are needed?
def home():
	if request.method == "POST":
		try:
		login_session['Quote'] = request.form['Quote']
		login_session['Name'] = request.form['Name'] 
		login_session['Age'] = request.form['Age']
		return render_template('thanks.html')
	else:
		except:
		return render_template('home.html')


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', ) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)