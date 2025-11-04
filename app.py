from flask import Flask

APP = Flask(__name__)

@APP.get("/")
def index():
    return "<h1>Ricardo Lucas!</h1>"
