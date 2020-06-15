from data_analysis.sentiment_analyzer import SentimentAnalyzer
from core.scrape.cleaner import Cleaner
from core.scrape.scrape_constants import NEWS_URLS, HEADLINE_MARKERS

analyzer = SentimentAnalyzer()
sentence = "She snubbed him out, brewing chaos and much more"
print("Liu and Hu:", analyzer.liu_and_hu_polarity(sentence))
print("VADER:", analyzer.vader_polarity(sentence))