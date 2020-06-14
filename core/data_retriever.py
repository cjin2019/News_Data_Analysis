from python_scrape.cleaner import Cleaner
from store_data.data_manager import DataManager

class DataRetriever:
    @staticmethod
    def gather_news_source_data(data_manager, news_outlet):
        cleaner = Cleaner(news_outlet)
        titles = cleaner.get_titles()
        for title in titles:
            print(f'adding {str(title)}')
            data_manager.insert_headline(str(title), news_outlet)

    @staticmethod
    def gather_all_data():
        data_manager = DataManager()

        for news_outlet in ['abc', 'fox', 'nbc', 'reuters']:
            print(f'inserting for {news_outlet}')
            DataRetriever.gather_news_source_data(
                data_manager,
                news_outlet
            )
        
        data_manager.close()
