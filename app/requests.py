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
        name = news_item.get('name')
        description = news_item.get('description')
        title = news_item.get('title')
        author = news_item.get('author')
        image = news_item.get('urlToImage')
        url = news_item.get('url')
        publishedAt = news_item.get('publishedAt')

        if image:
            news_object = News(name,title,author,image,url,publishedAt)
            news_results.append(news_object)
    return news_results

def get_article(id):
    get_article_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        news_object = None

        if article_details_response:
            id = article_details_response.get('id')
            description = article_details_response.get('description')
            title = article_details_response.get('title')
            author = article_details_response.get('author')
            image = article_details_response.get('urlToImage')
            url = article_details_response.get('url')
            publishedAt = article_details_response.get('publishedAt')

            news_object = News(id,description,title,author,image,url,publishedAt)

    return news_object