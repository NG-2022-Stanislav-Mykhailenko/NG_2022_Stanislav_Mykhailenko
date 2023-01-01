from flask import Flask, render_template, redirect, request
from datetime import datetime

app = Flask("Calculator")

@app.route('/')
def index():
	result = None
	if 'operation' in request.args:
		result = eval(request.args.get('operation'))
	return render_template("index.html", result=result)

app.run(port=8080)
