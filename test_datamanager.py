from store_data.data_manager import DataManager

if __name__ == '__main__':
	dbManager = DataManager()
	#dbManager.insert_headline_into_headlinestable('Test 1 Headline')
	# idNews = dbManager.get_id_for('NewsSource', 'Name', 'fox')
	# idHeadline = dbManager.get_id_for('Headline', 'Content', 'Test 1 Headline')
	# print("idNews:", idNews, "\tidHeadline:", idHeadline)
	dbManager.insert_headline('Test 2 Headline', 'fox')
	dbManager.close()