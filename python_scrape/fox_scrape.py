import os
from html_parser import HTMLParser
from cleaner import Cleaner
from constants import NEWS_URLS, HEADLINE_MARKERS

def create_directories(news_outlet):
    if not os.path.exists('output'):
        os.mkdir('output')
    if not os.path.exists(f'output/{news_outlet}'):
        os.mkdir(f'output/{news_outlet}')

def output_html(news_outlet):
    url = NEWS_URLS.get(news_outlet)

    print(f'outputing html at {url}')

    html_parser = HTMLParser(url)
    html_text = html_parser.get_html_text()
    html_parser.output_to_file(html_text, f'output/{news_outlet}/html_text.html')

if __name__ == "__main__":
    news_outlet = 'fox'

    create_directories(news_outlet)

    output_html(news_outlet)
    cleaner = Cleaner(news_outlet)
    clean_titles = cleaner.get_titles()
    HTMLParser.output_to_file(clean_titles, f'output/{news_outlet}/output.txt')

    # <h2 class="title title-color-default">
    # <li class="related-item title-color-default">
    # <li class="related-item related-item-color-default">


    # <header class="info-header">