# How To Make a Web Application Using Flask in Python 3
 This references: https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3


## Step 1 — Installing Flask
- Before activating the virtual environment, you need to make sure it has been created. The standard command to create a virtual environment is: **python3 -m venv env**
- activate the environment: **source env/bin/activate**
- your prompt will now have an env prefix that may look as follows: (env)@amyxg /foldername (main)
- To install Flask, run the following command: **pip install flask**

## Step 2 — Creating a Base Application
- you’ll make a small web application inside a Python file and run it to start the server, which will display some information on the browser. open a file named hello.py for editing: **nano hello.py** 
___in nano, use CTRL + O (to save) and CTRL + X (to exit)___
- To run your web application, you’ll first tell Flask where to find the application (the hello.py file in your case) with the FLASK_APP environment variable: **export FLASK_APP=hello**
- run it in development mode with the FLASK_ENV environment variable: **export FLASK_ENV=development**
- run the application using the flask run command: **flask run**
- create an app.py also

# Step 3 — Using HTML templates
- create a directory called templates inside your FlaskBootstrap directory: **mkdir templates**
- Then inside it, open a file called index.html for editing: **nano templates/index.html**
- create a directory called static inside your main FlaskBootstrap directory: **mkdir static**
- create the css directory inside the static directory: **mkdir static/css**
___css helps design/edit your html___
- create a file called base.html inside your templates directory: **nano templates/base.html**

# Step 4 — Setting up the Database
- create a .sql file that contains SQL commands to create the posts table with a few columns. You’ll then use this file to create the database.: **nano schema.sql**
* id: An integer that represents a primary key, this will get assigned a unique value by the database for each entry (that is a blog post).
* created: The time the blog post was created at. NOT NULL signifies that this column should not be empty and the DEFAULT value is the CURRENT_TIMESTAMP value, which is the time at which the post was added to the database. Just like id, you don’t need to specify a value for this column, as it will be automatically filled in.
* title: The post title.
* content: The post content.
- generate an SQLite .db database file: **nano init_db.py**
- run init_db.py in the terminal using the python command: **python init_db.py**
___Once the file finishes execution, a new file called database.db will appear in your FlaskBootstrap directory. This means you’ve successfully set up your database.___