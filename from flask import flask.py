from flask import flask
app=flask(_gta_)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"