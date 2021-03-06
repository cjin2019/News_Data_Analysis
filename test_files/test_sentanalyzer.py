from data_analysis.sentiment_analyzer import SentimentAnalyzer
from core.scrape.cleaner import Cleaner
from core.scrape.scrape_constants import NEWS_URLS, HEADLINE_MARKERS
from core.database.data_manager import DataManager

sentanalyzer = SentimentAnalyzer()
datamanager = DataManager()

liu_hu_scores = []
vader_scores  = []
textblob_scores = []
pattern_scores = []

ids_headlines = datamanager.get_all_ids_headlines()[:30]
for (i, headline) in ids_headlines:
	liu_hu_scores.append(sentanalyzer.liu_and_hu_polarity(headline))
	vader_scores.append(sentanalyzer.vader_polarity(headline))
	textblob_scores.append(sentanalyzer.retrieve_sentiment_textblob(headline))
	pattern_scores.append(sentanalyzer.retrieve_sentiment_pattern(headline))
	print("Headline:", headline)
	print("Liu and Hu:", liu_hu_scores[-1])
	print("Vader:", vader_scores[-1])
	print("TextBlob:", textblob_scores[-1])
	print("Pattern:", pattern_scores[-1])
datamanager.close()