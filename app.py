from flask import Flask, render_template, request
from databases import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iasas-food-is-good'

# TODO: Add all of the routes you want below this line!

@app.route("/login", methods = ['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		if get_user_by_mail(request.form['email']) != None and request.form['password'] == get_user_by_mail(request.form['email']).word:
			return render_template('homepage.html')
		return render_template('login.html')

@app.route("/signupsub", methods = ['GET','POST'])
def signup():
	if request.method == 'GET':
		return render_template("homepage.html")
	else:
		add_user(
			name=request.form['signupname'],
			email=request.form['signupemail'],
			word=request.form['signupword']
			 )

		return render_template("homepage.html")

@app.route("/")
def index():
	return render_template("homepage.html")


if __name__ == "__main__":
	app.run(host="localhost", port=8080, debug=True)