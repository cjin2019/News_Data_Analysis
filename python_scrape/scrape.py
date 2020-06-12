"""
Sources:
1. https://www.dataquest.io/blog/web-scraping-tutorial-python/
2. https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558
"""
import os
from python_scrape.html_parser import HTMLParser
from python_scrape.constants import NEWS_URLS

def create_directories():
    if not os.path.exists('output'):
        os.mkdir('output')
    for news_outlet in NEWS_URLS.keys():
        if not os.path.exists(f'output/{news_outlet}'):
            os.mkdir(f'output/{news_outlet}')

if __name__ == "__main__":
    create_directories()

    for news_outlet, url in NEWS_URLS.items():
        print(f'scraping from {url}')
        html_parser = HTMLParser(url)
        html_text = html_parser.get_html_text()
        html_parser.output_to_file(html_text, f'output/{news_outlet}/html_text.html')
        titles_list = html_parser.get_tag_text('a')
        html_parser.output_to_file(titles_list, f'output/{news_outlet}/output.txt')
