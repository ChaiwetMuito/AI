from multiprocessing import Process
import os
from flask import Flask, render_template
from test import predictSpeech
app = Flask(__name__)

@app.route('/')
def Home():
	return render_template('index.html')

@app.route('/SER')
def SER():
    result = predictSpeech()
    print(result)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8999)