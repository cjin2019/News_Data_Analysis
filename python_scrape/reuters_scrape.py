import os
from html_parser import HTMLParser
from constants import NEWS_URLS

def create_directories():
    if not os.path.exists('output'):
        os.mkdir('output')
    if not os.path.exists('output/abc'):
        os.mkdir(f'output/{news_outlet}')

if __name__ == "__main__":
    create_directories()

    news_outlet = 'reuters'
    url = NEWS_URLS.get(news_outlet)

    print(f'scraping from {url}')
    html_parser = HTMLParser(url)
    titles_list = html_parser.get_css_items_text('.story-title')
    html_parser.output_to_file(titles_list, f'output/{news_outlet}/output.txt')