from flask import Flask, render_template, redirect, request
from datetime import datetime

app = Flask("News")

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

app.run(port=8080)
