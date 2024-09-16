# minimal Flask app
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# Do any app specific setup here
# for instance, loading a database
app.config["DEBUG"] = True # will run in debug mode
#ro: make thiis a databasee or something
comments = []

@app.route("/", methods=["GET", "POST"]) # we allow posting
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)
    #otherwise, it's a post
    comments.append(request.form["contents"])
    return redirect(url_for('index'))

@app.route("/action")
def action():
    return "Hello from the action route!"
