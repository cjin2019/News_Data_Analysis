"""
Sources:
1. https://www.dataquest.io/blog/web-scraping-tutorial-python/
2. https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558
3. https://www.crummy.com/software/BeautifulSoup/bs4/doc/#tag
"""
import requests
from bs4 import BeautifulSoup

class HTMLParser:
    def __init__(self, url):
        self.url = url
        self.soup = self._soup()

    def _soup(self):
        page_content = self.get_html_content()
        soup = BeautifulSoup(page_content, 'html.parser')
        return soup

    def reset_soup(self):
        self.soup = self._soup()

    def get_html_content(self):
        """
        Returns HTML of url (in bytes)
        """
        r1 = requests.get(self.url)
        coverpage = r1.content
        return coverpage

    def get_html_text(self):
        """
        Returns html of webpage at url
        """
        return self.soup.prettify()
    
    def get_first_element_item(self, element):
        self.soup.find(element)

    def get_all_element_items(self, element):
        """
        Returns each instance of a given element
        in the HTML
        """
        return self.soup.find_all(element)

    def get_element_text(self, element):
        """
        Returns text for each instance of a given element
        in the HTML
        """
        raw_content = self.soup.find_all(element)

        return [content.get_text() for content in raw_content]

    def get_css_items(self, css_val):
        '''
        Returns all the items with a specific css val (eg. class)
        '''
        return self.soup.select(css_val)
    def get_css_items_text(self, css_val):
        '''
        Returns text for each instance of a given css item in
        HTML
        '''
        raw_content = self.soup.select(css_val)
        return [content.get_text() for content in raw_content]
    def decompose(self, element):
        items = self.get_all_element_items(element)

        for item in items:
            item.decompose()
    
    @staticmethod   
    def output_to_file(content, filepath):
        """
        Writes given content to file at a given filepath
        """
        with open(filepath, 'w', encoding='utf-8') as filename:
            if isinstance(content, list):
                for content_item in content:
                    filename.write(f'{content_item}\n')
            else:
                filename.write(str(content))
