from app import app
from flask import render_template, redirect, request, url_for
from .requests import get_news, get_article, search_article

@app.route ('/')
def index():

    # Getting popular news
    us_news = get_news('us')
    de_news = get_news('de')
    
    title = 'Home page for the News App'
    heading = "Welcome to your Favorite Modern News App"

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('search',news_title=search_article))
    else:
        return render_template('index.html', title = title, heading = heading, us = us_news, de = de_news)

@app.route('/news/<id>')
def news(id):
    
    #Getting articles
    article = get_article(id)
    title = f'{news.title}'

    return render_template('news.html',title = title, article = article)

@app.route('/search/<news_title>')
def search(news_title):

    #searching for an article
    article_title_list = news_title.split(" ")
    article_title_format = "+".join(article_title_list)
    searched_articles = search_article(article_title_format)
    title = f'search results for {news_title}'
    return render_template('search.html', news = searched_articles, title = title)