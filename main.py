import requests
import random
import time
from flask import Flask, request, render_template, Response

headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36'
}


app = Flask(__name__)
def getrandomduck():
    image_urls = requests.get(url=f'https://unsplash.com/napi/search/photos?page=30&per_page={random.randint(1,100)}&query=duck').json()
    while True:
        url = random.choice(image_urls['results'])['urls']['full']
        if "photo" in url:
            return url
@app.route('/duck')
def duck():
    return {"image":getrandomduck()},202

@app.route('/rawduck')
def rawduck():
    return render_template("rawduck__.html", user_image = getrandomduck())

if __name__ == '__main__':
    app.run()
