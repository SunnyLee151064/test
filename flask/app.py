import http
from tkinter.tix import MAIN
from unicodedata import name
from flask import Flask
from pip import main
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
