# Lesson 6 Task 2: web server system info
# Author: Stanislav Mykhailenko
# License: Unlicense

from databaseWorker import *
from flask import Flask, render_template, redirect, request
import platform, psutil, os

app = Flask("Computer info")
prepareDb("data.db")

@app.route('/')
def index():
    rows = getData("data.db")
    return render_template("index.html", data=generateDataHTMLTable(rows))

@app.route('/send')
def send():
	os.remove("data.db")
	prepareDb("data.db")

	if request.args.get('cpu'):
		sendData("data.db", "CPU", platform.processor())
	if request.args.get('ram'):
		sendData("data.db", "RAM", str(psutil.virtual_memory()))
	if request.args.get('architecture'):
		sendData("data.db", "Architecture", str(platform.architecture()))
	if request.args.get('family'):
		sendData("data.db", "Family", platform.machine())
	return redirect('/')

app.run(host='0.0.0.0', port=8081)
