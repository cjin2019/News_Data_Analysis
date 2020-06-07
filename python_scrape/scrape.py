"""
Sources:
1. https://www.dataquest.io/blog/web-scraping-tutorial-python/
2. https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558
"""
from html_parser import HTMLParser

if __name__ == "__main__":
    html_parser = HTMLParser('https://www.foxnews.com/')
    #html_parser = HTMLParser('https://www.nbcnews.com/')
    #html_parser.print_headlines_lxml()
    #html_text = html_parser.get_html_text()
    #html_parser.output_to_file(html_text, 'output/html_text.txt')
    titles_list = html_parser.get_element_text('a')
    html_parser.output_to_file(titles_list, 'output/output.txt')
