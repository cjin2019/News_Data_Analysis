import unittest
from data_analysis.sentence_parser import SentenceParser

class TestSentenceParser(unittest.TestCase):
	"""docstring for TestSentenceParser"""

	def setUp(self):
		"""
		Initializes with parser
		"""
		self.parser = SentenceParser()

	def test_case_1(self):
		sentence = "My name is Caroline"
		expected = {"My name", "Caroline"}
		res = set(self.parser.chunk_noun_phrases(sentence))
		self.assertEqual(res, expected)

	def test_case_2(self):
		sentence = "U.S. Supreme Court bans LGBT discrimination"
		expected = {"U.S. Supreme Court", "LGBT discrimination"}
		res = set(self.parser.chunk_noun_phrases(sentence))
		self.assertEqual(res, expected)

	def test_case_3a(self):
		sentence = "Parents beat 12-year-old boy together"
		expected = {"Parents", "12-year-old boy"}
		res = set(self.parser.chunk_noun_phrases(sentence))
		self.assertEqual(res, expected)

	def test_case_3b(self):
		sentence = "Father and son went to the store"
		expected = {"Father", "son", "store"}
		res = set(self.parser.chunk_noun_phrases(sentence))
		self.assertEqual(res, expected)

	def test_case_3c(self):
		sentence = "Father, mom, and son went to the store"
		expected = {"Father", "mom", "son", "store"}
		res = set(self.parser.chunk_noun_phrases(sentence))
		self.assertEqual(res, expected)

	def test_case_4(self):
		sentence = "Catherine and Caroline love to watch Demon Slayer and Haikyuu"
		expected = {"Catherine", "Caroline", "Demon Slayer", "Haikyuu"}
		res = set(self.parser.chunk_noun_phrases(sentence))
		self.assertEqual(res, expected)

	def test_case_noun_verb_a(self):
		sentence = "Father, son stab 12-year-old boy together"
		expected = {"Father", "son", "12-year-old boy"}
		res = set(self.parser.chunk_noun_phrases(sentence))
		self.assertEqual(res, expected)

	def test_case_noun_verb(self):
		sentence = "Father, son beat, stab, and hit 12-year-old boy together"
		expected = {"Father", "son", "12-year-old boy"}
		res = set(self.parser.chunk_noun_phrases(sentence))
		self.assertEqual(res, expected)
if __name__ == '__main__':
	unittest.main(verbosity=3, exit =True)
