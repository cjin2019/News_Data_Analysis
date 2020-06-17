##Note: need to create configuration file to access mysql
from core.database.data_manager import DataManager
data_manager = DataManager()
headlines = data_manager.get_headlines(news_source = "nbc")
print(len(headlines))
data_manager.close()