import os

import requests
from flask import Flask, send_file, Response, render_template
from bs4 import BeautifulSoup
import hashlib

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def get_pig_latin():
    url = "http://hidden-journey-62459.herokuapp.com/esultray/{}/"
    hashstr = hashlib.md5(get_fact().encode('utf8')).hexdigest()
    return url.format(hashstr)


@app.route('/')
def home():
    return render_template('base.jinja2', pig_latin=get_pig_latin())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

