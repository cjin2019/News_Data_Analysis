from html_parser import HTMLParser
from constants import NEWS_URLS, HEADLINE_MARKERS

class Cleaner:
    def __init__(self, news_outlet):
        self.news_outlet = news_outlet

    def get_titles(self):
        """
        Gets cleaned titles
        """
        titles = self.scrape_titles()
        return self.clean_titles(titles)

    def scrape_titles(self):
        """
        Scrapes titles from url
        """
        url = NEWS_URLS.get(self.news_outlet)
        
        print(f'scraping titles from {url}')

        html_parser = HTMLParser(url)
        html_parser.decompose_items(HEADLINE_MARKERS.get(self.news_outlet).get('decompose'))

        return html_parser.get_items_text(HEADLINE_MARKERS.get(self.news_outlet).get('extract'))

    def clean_titles(self, titles):
        """
        Clean list of titles
        """
        print('cleaning titles')

        clean_titles = []

        for title in titles:
            clean_title = title.strip()
            if len(clean_title) == 0:
                continue
            if clean_title in clean_titles:
                continue
            clean_titles.append(clean_title)
        
        return clean_titles
