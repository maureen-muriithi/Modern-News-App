import unittest
from models import Source


class SourceTest(unittest.Testcase):

    def setUp(self):
        self.new_source = Source("bbc-news","BBC-News","BBC-News", "South Africa's Cyril Ramaphosa abandons May Day rally after booing", "President Ramaphosa was forced to leave a May Day event after angry workers stormed the stage.", "http://www.bbc.co.uk/news/world-africa-61296810", "https://ichef.bbci.co.uk/news/1024/branded_news/054E/production/_124385310_mediaitem124385309.jpg", "Image caption, President Ramaphosa tried to calm the angry miners down to no avail\r\nSouth Africa's President Cyril Ramaphosa had to leave a May Day rally after workers stormed the stage where he was … [+2638 chars]", "2022-04-30T00:02:42Z" )
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
