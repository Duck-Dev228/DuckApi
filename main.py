import requests
import random
import time
from flask import Flask, render_template

headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36'
}


app = Flask(__name__)
def img(name:str) -> str:
    image_urls = requests.get(url=f'https://unsplash.com/napi/search/photos?page=30&per_page={random.randint(1,100)}&query={name}').json()
    while True:
        url = random.choice(image_urls['results'])['urls']['full']
        if "photo" in url:
            return url

@app.route('/duck')
def duck():
    return {"image":img("duck")},202

@app.route('/rawduck')
def rawduck():
    return render_template("rawduck__.html", user_image = img("duck"))

@app.route('/pig')
def duck():
    return {"image":img("pig")},202

@app.route('/rawpig')
def rawduck():
    return render_template("rawduck__.html", user_image = img("pig"))

@app.route('/cow')
def duck():
    return {"image":img("cow")},202

@app.route('/rawcow')
def rawduck():
    return render_template("rawduck__.html", user_image = img("cow"))

@app.route('/chicken')
def duck():
    return {"image":img("chicken")},202

@app.route('/rawchicken')
def rawduck():
    return render_template("rawduck__.html", user_image = img("chicken"))

@app.route('/cat')
def duck():
    return {"image":img("cat")},202

@app.route('/rawcat')
def rawduck():
    return render_template("rawduck__.html", user_image = img("cat"))

@app.route('/dog')
def duck():
    return {"image":img("dog")},202

@app.route('/rawdog')
def rawduck():
    return render_template("rawduck__.html", user_image = img("dog"))

@app.route('/goose')
def duck():
    return {"image":img("goose")},202

@app.route('/rawgoose')
def rawduck():
    return render_template("rawduck__.html", user_image = img("goose"))

@app.route('/turkey')
def duck():
    return {"image":img("turkey bird")},202

@app.route('/rawturkey')
def rawduck():
    return render_template("rawduck__.html", user_image = img("turkey bird"))
