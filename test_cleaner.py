import unittest
from core.scrape.cleaner import Cleaner

class TestCleaner(unittest.TestCase):
	"""docstring for TestCleaner"""

	def setUp(self):
		self.cleaner = Cleaner("fox")

	def test_case_1(self):
		sentence = ['hi', "Get a credit card for your side hustle ⁠— how it can help"]
		expected = ['hi', "Get a credit card for your side hustle ⁠- how it can help"]
		res = self.cleaner.clean_titles(sentence)
		return self.assertEqual(res, expected)

	def test_case_2(self):
		sentences = ['Hi my name is "Caroline"']
		expected = ["Hi my name is 'Caroline'"]
		res = self.cleaner.clean_titles(sentences)
		return self.assertEqual(res, expected)

	def test_case_3(self):
		sentences = ['Hi my name is "Caroline"', 
					 "Get a credit card for your side hustle ⁠— how it can help",
					 '"—"'
					]
		expected = ["Hi my name is 'Caroline'",
					"Get a credit card for your side hustle ⁠- how it can help",
					"'-'"]
		res = self.cleaner.clean_titles(sentences)
		return self.assertEqual(res, expected)

if __name__ == '__main__':
	unittest.main()