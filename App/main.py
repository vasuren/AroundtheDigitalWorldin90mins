from flask import Flask, render_template
from gateway import Gateway
import os

app = Flask(__name__)
port = int(os.getenv("PORT"))


@app.route('/')
def home():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=ce0c5d404829241dc9b2ddbd3cc25a73'
    # TODO: fix this asap, can`t be like that, object will be created with every request
    gate = Gateway()
    return render_template('layout.html', data=gate.get_data(url))


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = port)
