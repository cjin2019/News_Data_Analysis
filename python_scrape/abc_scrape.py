import os
from html_parser import HTMLParser
from constants import NEWS_URLS, HEADLINE_MARKERS

def create_directories():
    if not os.path.exists('output'):
        os.mkdir('output')
    if not os.path.exists('output/abc'):
        os.mkdir(f'output/{news_outlet}')

if __name__ == "__main__":
    create_directories()

    news_outlet = 'abc'
    url = NEWS_URLS.get('abc')

    print(f'scraping from {url}')
    html_parser = HTMLParser(url)
    html_parser.decompose_items(HEADLINE_MARKERS.get('abc').get('decompose'))
    html_text = html_parser.get_html_text()
    html_parser.output_to_file(html_text, f'output/{news_outlet}/html_text.html')
    titles_list = html_parser.get_items_text(HEADLINE_MARKERS.get('abc').get('extract'))
    html_parser.output_to_file(titles_list, f'output/{news_outlet}/output.txt')


    # <section id="main-container">
    # <article class="headlines inbox single row-item" 
    # <article class="hero-three row-item"
    # <ul class="headlines-ul">
    # <div class="headlines-li-div">
