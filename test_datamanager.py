from store_data.data_manager import DataManager
from python_scrape.cleaner import Cleaner

def get_headlines(news_source):
	cleaner = Cleaner(news_source)
	return cleaner.get_titles()

if __name__ == '__main__':
	dbManager = DataManager()
	news_source = 'fox'

	headlines = get_headlines(news_source)
	
	#dbManager.insert_headline_into_headlinestable('Test 1 Headline')
	# idNews = dbManager.get_id_for('NewsSource', 'Name', 'fox')
	# idHeadline = dbManager.get_id_for('Headline', 'Content', 'Test 1 Headline')
	# print("idNews:", idNews, "\tidHeadline:", idHeadline)
