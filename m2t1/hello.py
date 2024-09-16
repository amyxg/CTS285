# minimal Flask app
from flask import Flask, render_template

app = Flask(__name__)
# Do any app specific setup here
# for instance, loading a database
app.config["DEBUG"] = True # will run in debug mode

@app.route("/")
def index():
    # find the template in /templates
    #name = "Amy"
    return render_template("main_page.html")

@app.route("/action")
def action():
    return "Hello from the action route!"
