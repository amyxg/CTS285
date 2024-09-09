# minimal Flask app
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h3>Hello, World!</h3>"