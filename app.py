from flask import Flask, request, render_template, redirect, after_this_request
from flask import send_file
import os
import time
import shutil
import datetime
import random
import os

app = Flask(__name__)


@app.route('/')
def my_form():
    try:
        if request.args.get('url') != None:
            try:
                shutil.rmtree('./tmp')
            finally:
                pass
            url = request.args.get('url')
            now = datetime.datetime.now()
            now_str = now.strftime("%d-%m-%Y-%H-%M-%S%f")
            file_id = now_str + "-" + str(random.randint(1, 100))
            print(file_id)
            os.popen(f"youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a] --output ./tmp/{file_id}/video.mp4 {url}").read()
            return redirect("/download/" + file_id)
        else:
            return render_template('index.html')
    finally:
        pass

@app.route('/', methods=['POST'])
def my_form_post():
    now = datetime.datetime.now()
    now_str = now.strftime("%d-%m-%Y-%H-%M-%S%f")
    file_id = now_str + "-" + str(random.randint(1, 100))
    print(file_id)
    url = request.form['text']
    os.popen(f"youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a] --output ./tmp/{file_id}/video.mp4 {url}").read()
    return redirect("/download/" + file_id)



@app.route(f'/download/<url_id>')
def downloadFile(url_id):
    # For windows you need to use drive name [ex: F:/Example.pdf]
    path = f"./tmp/{url_id}/video.mp4"
    return send_file(path, as_attachment=True)
