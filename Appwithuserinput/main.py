from flask import Flask, render_template, request
from gateway import Gateway
import os


app = Flask(__name__)
port = int(os.getenv("PORT"))

@app.route('/')
def TakeInput():
    
	return render_template('Inputform.html')


@app.route('/result',methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        lat = request.form['Latitude']
        lon = request.form['Longitude']
        url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=ce0c5d404829241dc9b2ddbd3cc25a73'
        # TODO: fix this asap, can`t be like that, object will be created with every request
        gate = Gateway()
        data = gate.get_data(url)
        return render_template('layout.html',data = data)


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = port, debug = False)