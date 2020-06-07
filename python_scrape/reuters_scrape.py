import os
from html_parser import HTMLParser
from constants import NEWS_URLS, headline_markers

def create_directories():
    """
    Returns a new directory
    """
    if not os.path.exists('output'):
        os.mkdir('output')
    if not os.path.exists('output/abc'):
        os.mkdir(f'output/{news_outlet}')
def get_headlines(parser, news):
    """
    Returns a list of the headlines
    """
    css_vals = []
    identifiers = headline_markers[news]
    for css_type in identifiers:
        css_vals = css_vals + parser.get_all_css_format(identifiers[css_type], css_type)
    titles_list = [title.strip() for title in parser.get_css_items_text(css_vals)]
    return titles_list

if __name__ == "__main__":
    create_directories()

    news_outlet = 'reuters'
    url = NEWS_URLS.get(news_outlet)

    print(f'scraping from {url}')
    html_parser = HTMLParser(url)

    titles_list = get_headlines(html_parser, news_outlet)
    #get_headlines(html_parser, news_outlet)
    html_parser.output_to_file(titles_list, f'output/{news_outlet}/output.txt')