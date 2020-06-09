from html_parser import HTMLParser
from constants import NEWS_URLS, HEADLINE_MARKERS, remove_strs

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
        if 'decompose' in HEADLINE_MARKERS[self.news_outlet]:
            html_parser.decompose_items(HEADLINE_MARKERS.get(self.news_outlet).get('decompose'))
        if 'extract' in HEADLINE_MARKERS[self.news_outlet]:
            return html_parser.get_items_text(HEADLINE_MARKERS.get(self.news_outlet).get('extract'))
        return []

    def remove_str(self, title):
        """
        Removes unnecessary string
        """
        for remove_str in remove_strs:
            title = title.replace(remove_str, '')
        return title
    def clean_titles(self, titles):
        """
        Clean list of titles
        """
        print('cleaning titles')

        clean_titles = []

        for title in titles:
            clean_title = self.remove_str(title.strip())
            if len(clean_title) == 0:
                continue
            if clean_title in clean_titles:
                continue
            clean_titles.append(clean_title)
        
        return clean_titles
