from bs4 import BeautifulSoup
from flask import Flask, render_template, request, send_from_directory
from zipfile import ZipFile
import os, requests, threading, uuid, urllib.request

app = Flask("Image download")

if not os.path.exists("download"):
    os.makedirs("download")

if not os.path.exists("upload"):
    os.makedirs("upload")

def downloadImage(url, image, directory):
	try:
		image_link = image["src"]
	except:
		pass

	try:
		filename = image_link.split("/")[-1]
		urllib.request.urlretrieve(url + image_link, directory + "/" + filename)
	except:
		pass

def downloadImages(url, uuid):
	directory = "download/" + uuid
	filename = "upload/" + uuid + ".zip"
	os.mkdir(directory)
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	images = soup.findAll('img')
	for image in images:
		downloadImage(url, image, directory)

	with ZipFile(filename, 'w') as zip:
		for path, directories, files in os.walk(directory):
			for file in files:
				file_name = os.path.join(path, file)
				zip.write(file_name)

	return "<a href=\"" + filename + "\">Image archive</a>"

@app.route('/')
def index():
	result = None
	if 'url' in request.args:
		response = downloadImages(request.args.get('url'), str(uuid.uuid4()))
	return render_template("index.html", response=response)

@app.route('/upload/<path:filename>')
def download(filename):
	return send_from_directory("upload", filename)

app.run(host='0.0.0.0', port=8081)
