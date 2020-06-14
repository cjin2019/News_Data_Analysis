
from core.database.database_interactor import DatabaseInteractor
from core.database.constants import DATABASE_NAME
from config import USER_INFO

class DataManager:
	
	def __init__(self):
		self.db_interactor = DatabaseInteractor(USER_INFO['user'], password = USER_INFO['password'])
		self.db_interactor.choose_database(DATABASE_NAME)

	def insert_headline(self, headline, news_source):
		"""
		Updates the database when inserting the headline
		"""
		insert_cmd = f'INSERT INTO Headline (Content) VALUES ("{headline}");'
		self.db_interactor.change_one_sql_command(insert_cmd)
		idNews = self.get_id('NewsSource', 'Name', news_source)
		idHeadline = self.get_id('Headline', 'Content', headline)

		insert_cmd = f'INSERT INTO NewsSourceHeadline (NewsSourceId, HeadlineId) \
					   VALUES ({idNews},{idHeadline});'
		self.db_interactor.change_one_sql_command(insert_cmd)

	def get_id(self, tble_name, column_name, item_value):
		"""
		Returns the id given the item_value in a column for a table
		"""
		sql_value = item_value
		if type(item_value)==str:
			sql_value = f'"{item_value}"'

		fetch_cmd = f'SELECT * FROM {tble_name} WHERE {column_name} = {sql_value};'

		##Assumes the Id is the first value in the tuple
		row = self.db_interactor.fetch_one_sql_command(fetch_cmd)
		return row[0][0]

	def close(self):
		"""
		Closes the database interactor. Don't forget to do this!
		"""
		self.db_interactor.close()

	