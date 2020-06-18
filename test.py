##Note: need to create configuration file to access mysql
from core.database.data_manager import DataManager
from data_analysis.keyword_retriever import KeywordRetriever

data_manager = DataManager()
# keyword = input("Type in a search word: ")
headlines = data_manager.get_headlines()
# print("Headlines:")
# for headline in headlines:
# 	print(headline)
keyword_retriever = KeywordRetriever()
keywords = keyword_retriever.get_keywords(headlines)
print("Keywords:")
for phrase in keywords:
	print(phrase)
data_manager.close()