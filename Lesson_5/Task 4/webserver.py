from flask import Flask, render_template, redirect, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask("News")
auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("example")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
def index():
	with open("articles.txt", "r") as file:
		data = file.read()
	return render_template("index.html", contents=data)

@app.route('/editor')
def editor():
	return render_template("editor.html")

@app.route('/process.html')
def process():
	with open("articles.txt", "a") as file:
		file.write("<h1>" + str(request.args.get('title')) + "</h1>\n<h4>" + str(datetime.now()) + "</h4>\n<h2>" + str(request.args.get('text')) + "</h2><hr>\n")
	return redirect('/')

@app.route('/admin')
@auth.login_required
def admin():
	with open("articles.txt", "r") as file:
		data = file.read()
	return render_template("admin.html", contents=data)

@app.route('/process_admin.html')
@auth.login_required
def process_admin():
	with open("articles.txt", "w") as file:
		file.write(str(request.args.get('data')))
	return redirect('/')

app.run(port=8080)
