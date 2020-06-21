from core.scrape.cleaner import Cleaner
from core.database.data_manager import DataManager

class DataRetriever:
    def add_key_words(self, data_manager, title):
        keywords = [] # add algorithm to get keywords
        for keyword in keywords:
            data_manager.insert_keyword(keyword)

    def add_sentiment_values(self, data_manager, title):
        vader = 0 # add calculation for Vader
        liu_hu = 0 # add calculation for Liu-Hu

        data_manager.insert_sentiment_values(title, vader, liu_hu)

    def gather_news_source_data(self, data_manager, news_outlet):
        cleaner = Cleaner(news_outlet)
        titles = cleaner.get_titles()
        for title in titles:
            print(f'adding {str(title)}')
            data_manager.insert_headline(str(title), news_outlet)

            #print(f'adding {str(title)}\'s sentiment values')
            #self.add_sentiment_values(data_manager, title)

            #print(f'adding {str(title)}\'s sentiment values key words')
            #self.add_key_words(data_manager, title)

    def gather_all_data(self):
        data_manager = DataManager()

        for news_outlet in ['abc', 'fox', 'nbc', 'reuters']:
            print(f'inserting for {news_outlet}')
            self.gather_news_source_data(
                data_manager,
                news_outlet
            )
        
        data_manager.close()
