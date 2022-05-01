from app import app

class News:

    def __init__(self,name,author,title, image, url, publishedAt):
        self.name = name
        self.title = title
        self.author = author
        self.url = url
        self.image = image
        self.publishedAt = publishedAt
        