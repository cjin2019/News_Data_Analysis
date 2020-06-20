##Note: need to create configuration file to access mysql
import unittest
from core.database.data_manager import DataManager

class TestDataManager(unittest.TestCase):
	"""docstring for TestDataManager"""

	def setUp(self):
		"""
		Initializes the data manager
		"""
		self.datamanager = DataManager()

	def tearDown(self):
		"""
		Closes the data manager
		"""
		self.datamanager.close()

class TestSQLCommand(TestDataManager):
	"""Checks to see if SQL statements are properly written"""

	def test_case_1(self):
		inp = [('Trump', 'Biden'), 'Floyd']
		expected = '((Headline.Content LIKE "%Trump%" AND Headline.Content LIKE "%Biden%") OR Headline.Content LIKE "%Floyd%")'
		res = self.datamanager.helper_OR(inp)
		self.assertEqual(res, expected)

	def test_case_2(self):
		inp = ['Trump']
		expected = '(Headline.Content LIKE "%Trump%")'
		res = self.datamanager.helper_OR(inp)
		self.assertEqual(res, expected)

class TestQueryKeyWords(TestDataManager):
	"""Only checks length! May need to update when more rows are added!"""

	def test_case_1(self):
		inp = [('Trump', 'Biden'), 'Floyd']
		expected = 24
		res = len(self.datamanager.get_headlines_with_keywords(inp))
		self.assertEqual(res, expected)

	def test_case_2(self):
		inp = ['Trump']
		expected = 73
		res = len(self.datamanager.get_headlines_with_keywords(inp))
		self.assertEqual(res, expected)

	def test_case_3(self):
		inp = ['Trump', 'Biden']
		expected = 84
		res = len(self.datamanager.get_headlines_with_keywords(inp))
		self.assertEqual(res, expected)

if __name__ == '__main__':
	unittest.main()
# data_manager = DataManager()
# # keyword = input("Type in a search word: ")
# headlines = data_manager.get_headlines()
# # print("Headlines:")
# # for headline in headlines:
# # 	print(headline)
# keyword_retriever = KeywordRetriever()
# keywords = keyword_retriever.get_keywords(headlines)
# print("Keywords:")
# for phrase in keywords:
# 	print(phrase)
# data_manager.close()