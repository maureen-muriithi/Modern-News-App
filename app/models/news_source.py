from app import app

class Source:

    def __init__(self, id, name, author,title, description, url, image, publishedAt, content):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.publishedAt = publishedAt
        self.content = content