import requests
import random
import threading
import time
from flask import Flask, render_template

headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36'
}

def DontSleep():
    print('duckquack')
    time.sleep(5)

dontsleep = threading.Thread(target=DontSleep,daemon=True)
dontsleep.start()


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
def pig():
    return {"image":img("pig")},202

@app.route('/rawpig')
def rawpig():
    return render_template("rawduck__.html", user_image = img("pig"))

@app.route('/cow')
def cow():
    return {"image":img("cow")},202

@app.route('/rawcow')
def rawcow():
    return render_template("rawduck__.html", user_image = img("cow"))

@app.route('/chicken')
def chicken():
    return {"image":img("chicken")},202

@app.route('/rawchicken')
def rawchicken():
    return render_template("rawduck__.html", user_image = img("chicken"))

@app.route('/cat')
def cat():
    return {"image":img("cat")},202

@app.route('/rawcat')
def rawcat():
    return render_template("rawduck__.html", user_image = img("cat"))

@app.route('/dog')
def dog():
    return {"image":img("dog")},202

@app.route('/rawdog')
def rawdog():
    return render_template("rawduck__.html", user_image = img("dog"))

@app.route('/goose')
def goose():
    return {"image":img("goose")},202

@app.route('/rawgoose')
def rawgoose():
    return render_template("rawduck__.html", user_image = img("goose"))

@app.route('/turkey')
def turkey():
    return {"image":img("turkey bird")},202

@app.route('/rawturkey')
def rawturkey():
    return render_template("rawduck__.html", user_image = img("turkey bird"))


