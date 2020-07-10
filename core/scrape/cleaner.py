from core.scrape.html_parser import HTMLParser
from core.scrape.scrape_constants import NEWS_URLS, HEADLINE_MARKERS, REMOVE_STRS, REPLACE_STRS

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

    def clean_title(self, title):
        """
        Removes unnecessary string
        """
        clean_title = title.strip()
        clean_title = clean_title.encode('utf-8', 'ignore').decode('utf-8')
        for remove_str in REMOVE_STRS:
            clean_title = clean_title.replace(remove_str, '')
        clean_title = self.replace_strs(clean_title)
        if len(clean_title) == 0:
            return
        
        return clean_title

    def replace_strs(self, title):
        """
        Replace the old char with the new char
        """
        clean_title = title
        for old_char in REPLACE_STRS:
            clean_title = clean_title.replace(old_char, REPLACE_STRS[old_char])
        return clean_title

    def clean_titles(self, titles):
        """
        Clean list of titles
        """
        print('cleaning titles')

        clean_titles = []

        for title in titles:
            clean_title = self.clean_title(title)
            if clean_title in clean_titles:
                continue
            if clean_title:
                clean_titles.append(clean_title)
        
        return clean_titles
