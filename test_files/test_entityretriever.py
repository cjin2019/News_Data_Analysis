from core.scrape.cleaner import Cleaner
from core.scrape.scrape_constants import NEWS_URLS, HEADLINE_MARKERS
from core.database.data_manager import DataManager

from data_analysis.sentence_parser import SentenceParser

sentenceparser = SentenceParser()
datamanager = DataManager()

ids_headlines = datamanager.get_all_ids_headlines()

# while(True):
# 	input_text = input("A number from 0 to 859, inclusive, or quit to end: ")
# 	if input_text=="quit":
# 		break
# 	else:
# 		idx = int(input_text)
# 		headline = ids_headlines[idx][1]
# 		print("Headline:", headline)
# 		print("Entities:", sentenceparser.retrieve_keywords(headline))
for idx, headline in ids_headlines:
	print("Headline:", headline)
	print("Entities:", sentenceparser.retrieve_keywords(headline))

datamanager.close()