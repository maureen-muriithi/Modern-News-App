from app import app
from flask import render_template
from .requests import get_news

@app.route ('/')
def headers():

    # Getting popular news
    us_news = get_news('us')
    de_news = get_news('de')
    print(us_news)
    title = 'Home page for the News App'
    heading = "Welcome to your Favorite Modern News App"
    return render_template('index.html', title = title, heading = heading, us = us_news, de = de_news)
