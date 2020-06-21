from data_analysis.sentence_cleaner import SentenceCleaner
import unittest

class TestSentenceCleaner(unittest.TestCase):

	def setUp(self):
		self.sentencecleaner = SentenceCleaner()

class TestCleanWord(TestSentenceCleaner):

	def test_case_1(self):
		text = "Hello!"
		expected = "Hello"
		res = self.sentencecleaner.clean_entity_text(text)
		self.assertEqual(res, expected)

	def test_case_2(self):
		text = "Kavanaugh rips "
		expected = "Kavanaugh"
		res = self.sentencecleaner.clean_entity_text(text)
		self.assertEqual(res, expected)

	def test_case_3(self):
		text = " the Milky Way"
		expected = "Milky Way"
		res = self.sentencecleaner.clean_entity_text(text)
		self.assertEqual(res, expected)

	def test_case_4(self):
		text = "Like the Statue"
		expected = "Like the Statue"
		res = self.sentencecleaner.clean_entity_text(text)
		self.assertEqual(res, expected)

	def test_case_5(self):
		text = "     Kavanaugh rips    "
		expected = "Kavanaugh"
		res = self.sentencecleaner.clean_entity_text(text)
		self.assertEqual(res, expected)
if __name__ == '__main__':
	unittest.main()