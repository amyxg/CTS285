# minimal Flask app
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # three quotes for multiline strings
    return """
    <h3>Hello, World!</h3>
    <p>This is a paragraph</p>
    <a href="action">Click Here</a>

    """
@app.route("/action")
def action():
    return "Hello from the action route!"
