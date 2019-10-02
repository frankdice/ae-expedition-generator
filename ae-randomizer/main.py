#! /usr/bin/env python

from randomizer import AERandomizer
from flask import Flask

app = Flask(__name__)

@app.route('/')
def landing():
  return "AE Randomizer"

@app.route('/begin-expedition')
def new_expedition():
  aer = AERandomizer()
  return aer.begin_expedition()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
