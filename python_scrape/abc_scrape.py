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

def extract_titles(news_outlet):
    url = NEWS_URLS.get(news_outlet)
    
    print(f'scraping from {url}')

    html_parser = HTMLParser(url)
    html_parser.decompose_items(HEADLINE_MARKERS.get(news_outlet).get('decompose'))

    titles = html_parser.get_items_text(HEADLINE_MARKERS.get(news_outlet).get('extract'))
    return titles

def clean_titles(titles):
    print('cleaning titles')

    clean_titles = []

    for title in titles:
        clean_title = title.strip()
        if len(clean_title) > 0:
            clean_titles.append(clean_title)
    
    return clean_titles

if __name__ == "__main__":
    news_outlet = 'abc'

    create_directories(news_outlet)

    output_html(news_outlet)
    cleaner = Cleaner(news_outlet)
    clean_titles = cleaner.get_titles()
    HTMLParser.output_to_file(clean_titles, f'output/{news_outlet}/output.txt')

    # <section id="main-container">
    # <article class="headlines inbox single row-item" 
    # <article class="hero-three row-item"
    # <ul class="headlines-ul">
    # <div class="headlines-li-div">
