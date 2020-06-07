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

    news_outlet = 'abc'
    url = NEWS_URLS.get('abc')

    print(f'scraping from {url}')
    html_parser = HTMLParser(url)
    html_parser.decompose('nav')
    titles_list = html_parser.get_element_text('a')
    html_parser.output_to_file(titles_list, f'output/{news_outlet}/output.txt')


# remove: <nav>
# remove: <article class="_footer">

    # <section id="main-container">
    # <article class="headlines inbox single row-item" 
    # <article class="hero-three row-item"
    # <ul class="headlines-ul">
    # <div class="headlines-li-div">
