# Lesson 6 Task 1: web chat
# Author: Stanislav Mykhailenko
# License: Unlicense

from databaseWorker import *
from flask import Flask, render_template, redirect, request

app = Flask("Chat")
prepareDb("messages.db")

@app.route('/')
def index():
    rows = getMessages("messages.db")
    return render_template("index.html", messages=generateMessagesHTMLTable(rows))

@app.route('/send')
def send():
    nickname = request.args.get('nickname')
    message = request.args.get('message')
    sendMessage("messages.db", nickname, message)
    return redirect('/')

@app.route('/getMessagesTable')
def getMessagesTable():
    rows = getMessages("messages.db")
    return generateMessagesHTMLTable(rows)

app.run(host='0.0.0.0', port=8081)
