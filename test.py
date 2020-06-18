##Note: need to create configuration file to access mysql
from core.database.data_manager import DataManager
data_manager = DataManager()
keyword = input("Type in a search word: ")
headlines = data_manager.get_headlines_with_keyword(keyword)
print("Headlines:")
for headline in headlines:
	print(headline)
data_manager.close()