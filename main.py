from flask import Flask, render_template
from gateway import Gateway

app = Flask(__name__)


@app.route('/')
def home():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=2de143494c0b295cca9337e1e96b00e0'
    # TODO: fix this asap, can`t be like that, object will be created with every request
    gate = Gateway()
    return render_template('layout.html', data=gate.get_data(url))


if __name__ == '__main__':
    app.debug = True
    app.run()
