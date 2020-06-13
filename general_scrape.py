import os
from python_scrape.html_parser import HTMLParser
from python_scrape.cleaner import Cleaner
from python_scrape.constants import NEWS_URLS, HEADLINE_MARKERS

def create_directories(news_outlet):
    """
    Returns a new directory
    """
    if not os.path.exists('output'):
        os.mkdir('output')
    if not os.path.exists('output/' + news_outlet):
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
    print('Type one of the following news outlets: abc, fox, cnn, nbc, reuters, below')
    news_outlet = input('News Outlet:')
    create_directories(news_outlet)
    output_html(news_outlet)
    update_outputtxt(news_outlet)