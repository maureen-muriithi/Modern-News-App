
from app import app
import urllib.request, json
from .models import news

News = news.News

api_key = app.config['NEWS_API_KEY']               # Allows us to get the  api key for the news app

base_url = app.config['NEWS_API_BASE_URL']          # Allows us to get the base url for the news app

def get_news(country):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(country, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        image = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
        
        if image:
            news_object = News(id, name, author, title, description, url, image, publishedAt, content)
            news_results.append(news_object)
    return news_results

def get_article(news_name):
    get_article_details_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(news_name, api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        news_object = None

        if article_details_response:
            id = article_details_response.get('id')
            name = article_details_response.get('name')
            author = article_details_response.get('author')
            title = article_details_response.get('title')
            description = article_details_response.get('description')
            url = article_details_response.get('url')
            image = article_details_response.get('urlToImage')
            publishedAt = article_details_response.get('publishedAt')
            content = article_details_response.get('content')
            
            news_object = News(id, name, author, title, description, url, image, publishedAt, content)

    return news_object

def search_article(news_title):
    search_article_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(news_title, api_key)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_results(search_article_list)


    return search_article_results