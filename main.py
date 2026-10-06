from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/name")
def name():
    return "<h1>Hi, Divin Franco Manzi from Enterprise Web Dev!</h1>"