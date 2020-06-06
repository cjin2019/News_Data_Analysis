"""
Sources:
1. https://www.dataquest.io/blog/web-scraping-tutorial-python/
2. https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558
"""
import requests
from bs4 import BeautifulSoup

class HTMLParser:
    def __init__(self, url):
        self.url = url

    def get_html_content(self):
        """
        Returns HTML of url (in bytes)
        """
        r1 = requests.get(self.url)
        coverpage = r1.content
        return coverpage

    def get_html_text(self):
        page_content = self.get_html_content()
        soup = BeautifulSoup(page_content, 'html.parser')
        return soup.prettify()

    def get_element_text(self, element):
        page_content = self.get_html_content()
        soup = BeautifulSoup(page_content, 'html.parser')
        raw_content = soup.find_all(element)

        return [content.get_text() for content in raw_content]
    