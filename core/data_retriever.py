from core.scrape.cleaner import Cleaner
from core.database.data_manager import DataManager
from core.data_analysis.sentiment_analyzer import SentimentAnalyzer
from core.data_analysis.sentence_parser import SentenceParser

class DataRetriever:
    def gather_all_data(self):
        data_manager = DataManager()

        for news_outlet in ['abc', 'fox', 'nbc', 'reuters']:
            print(f'inserting for {news_outlet}')
            self.gather_news_source_data(
                data_manager,
                news_outlet
            )
        
        data_manager.close()
    
    def gather_news_source_data(self, data_manager, news_outlet):
        cleaner = Cleaner(news_outlet)
        titles = cleaner.get_titles()
        for title in titles:
            print(f'adding {str(title)}')
            data_manager.insert_headline(str(title), news_outlet)

            print(f'adding {str(title)}\'s sentiment values')
            self._add_sentiment_values(data_manager, title)

            print(f'adding {str(title)}\'s sentiment values key words')
            self._add_key_words(data_manager, title)

    def _add_sentiment_values(self, data_manager, title):
        sentiment_analyzer = SentimentAnalyzer()
        vader = sentiment_analyzer.vader_polarity(title)
        liu_hu = sentiment_analyzer.liu_and_hu_polarity(title)

        data_manager.insert_sentiment_values(title, vader, liu_hu)
    
    def _add_key_words(self, data_manager, title):
        sentence_parser = SentenceParser()
        keywords = sentence_parser.retrieve_keywords(title)
        for keyword in keywords:
            data_manager.insert_keyword(keyword)
