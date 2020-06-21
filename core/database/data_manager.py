
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
		idNews = self.get_rows('NewsSource', 'Name', news_source)[0][0]
		insert_cmd = f'INSERT INTO Headline (Content, NewsSourceId) VALUES ("{headline}", {idNews});'
		self.db_interactor.change_one_sql_command(insert_cmd)

	def get_rows(self, tble_name, column_name, item_value):
		"""
		Returns the id given the item_value in a column for a table
		"""
		sql_value = item_value
		if type(item_value)==str:
			sql_value = f'"{item_value}"'

		fetch_cmd = f'SELECT * FROM {tble_name} WHERE {column_name} = {sql_value};'

		rows = self.db_interactor.fetch_one_sql_command(fetch_cmd)
		return rows

	def get_headlines_with_keyword(self, keyword):
		"""
		Returns a list of headlines with the keyword
		"""
		fetch_cmd = f'SELECT Headline.Content \
					  FROM Headline \
					  WHERE Headline.Content \
					  LIKE "%{keyword}%"'
		rows = self.db_interactor.fetch_one_sql_command(fetch_cmd)
		if rows == None:
			return []
		return [row[0] for row in rows]


	def get_headlines(self, news_source = None):
		"""
		Returns a list of headlines for a new source
		if news_source is None, return all headlines
		"""
		if news_source==None:
			return [row[1] for row in self.get_all_ids_headlines()]

		fetch_cmd = f'SELECT Headline.Content \
					FROM (Headline \
					INNER JOIN NewsSource \
					ON NewsSourceHeadline.NewsSourceId = NewsSource.Id) \
					WHERE NewsSource.Name = "{news_source}"'

		rows = self.db_interactor.fetch_one_sql_command(fetch_cmd)
		return [row[0] for row in rows]

	def get_all_ids_headlines(self):
		"""
		Returns a list of tuples (id, headline)
		"""
		fetch_cmd = f'SELECT Headline.Id, Headline.Content FROM Headline'

		##Headline is the first index
		rows = self.db_interactor.fetch_one_sql_command(fetch_cmd)
		return rows

	def close(self):
		"""
		Closes the database interactor. Don't forget to do this!
		"""
		self.db_interactor.close()

	