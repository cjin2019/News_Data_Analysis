import os
from html_parser import HTMLParser
from cleaner import Cleaner
from constants import NEWS_URLS, HEADLINE_MARKERS

def create_directories():
    """
    Returns a new directory
    """
    if not os.path.exists('output'):
        os.mkdir('output')
    if not os.path.exists('output/abc'):
        os.mkdir(f'output/{news_outlet}')

def output_html(news_outlet):
    url = NEWS_URLS.get(news_outlet)

    print(f'outputing html at {url}')

    html_parser = HTMLParser(url)
    html_text = html_parser.get_html_text()
    HTMLParser.output_to_file(html_text, f'output/{news_outlet}/html_text.html')

def update_outputtxt(news_outlet):
    cleaner = Cleaner(news_outlet)

    print(f'outputing titles for {news_outlet}')
    titles = cleaner.get_titles()
    HTMLParser.output_to_file(titles, f'output/{news_outlet}/output.txt')
if __name__ == '__main__':
    create_directories()
    print('Type one of the following news outlets: abc, fox, cnn, nbc, reuters, below')
    news_outlet = input('News Outlet:')
    output_html(news_outlet)
    update_outputtxt(news_outlet)