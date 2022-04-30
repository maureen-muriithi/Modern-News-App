from app import app
from flask import render_template

@app.route ('/')
def headers():
    title = 'Home page for the News App'
    heading = "Welcome to your Favorite Modern News App"
    return render_template("index.html", title = title, heading = heading)