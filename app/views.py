from app import app
from flask import render_template
from .requests import get_news, get_article

@app.route ('/')
def index():

    # Getting popular news
    us_news = get_news('us')
    de_news = get_news('de')
    
    title = 'Home page for the News App'
    heading = "Welcome to your Favorite Modern News App"
    return render_template('index.html', title = title, heading = heading, us = us_news, de = de_news)

@app.route('/news/<id>')
def news(id):
    
    #Getting articles
    article = get_article(id)
    title = f'{news.title}'

    return render_template('news.html',title = title, article = article)