
import unittest
from models import news

News = news.News

class NewsTest(unittest.Testcase):

    def setUp(self):
        self.new_news = News("9to5Mac","Filipe Espósito", "20 years after the eMac, should Apple introduce a new entry-level Mac?", "https://i0.wp.com/9to5mac.com/wp-content/uploads/sites/6/2022/04/Apple-eMac.jpeg?resize=1200%2C628&quality=82&strip=all&ssl=1", "2022-04-30T00:02:42Z" )
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

    if __name__ == '__main__':
        unittest.main()