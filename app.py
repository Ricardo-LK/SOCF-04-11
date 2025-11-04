from flask import Flask

APP = Flask(__name__)

@APP.get("/")
def index():
    return "<h1>Olá mundo!</h1>"
