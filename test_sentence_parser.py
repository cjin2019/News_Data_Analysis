import unittest
from core.data_analysis.sentence_parser import SentenceParser
from test_cases.test_sentence_parser_cases.input import SENTENCES
from test_cases.test_sentence_parser_cases.output import OUTPUTS

class TestSentenceParser(unittest.TestCase):
	"""docstring for TestSentenceParser"""

	def setUp(self):
		"""
		Initializes with parser
		"""
		self.parser = SentenceParser()

class TestChunkNounPhrase(TestSentenceParser):
	"""docstring for TestChunkNounPhrase"""

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
		sentence = "Parents beat and stab 12-year-old boy together"
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

	def test_case_5(self):
		sentence = "Beijing braces for 2nd wave of COVID-19 infections"
		expected = {"Beijing", "2nd wave", "COVID-19 infections"}
		res = set(self.parser.chunk_noun_phrases(sentence))
		self.assertEqual(res, expected)

	def test_case_6(self):
		sentence = "Bishop resumes work as Vatican abuse probe wraps"
		expected = {"Bishop", "work", "Vatican abuse probe"}
		res = set(self.parser.chunk_noun_phrases(sentence))
		self.assertEqual(res, expected)

	def test_case_noun_verb_a(self):
		sentence = "Father, son stab 12-year-old boy together"
		expected = {"Father", "son", "12-year-old boy"}
		res = set(self.parser.chunk_noun_phrases(sentence))
		self.assertEqual(res, expected)

	def test_case_noun_verb(self):
		sentence = "Father, son beat and stab 12-year-old boy together"
		expected = {"Father", "son", "12-year-old boy"}
		res = set(self.parser.chunk_noun_phrases(sentence))
		self.assertEqual(res, expected)

class TestCleanWord(TestSentenceParser):
	"""docstring for TestCleanWord"""

	def test_case_remove_punct(self):
		text = "'Political Machine'"
		expected = "Political Machine"
		res = self.parser.remove_punct(text)
		self.assertEqual(res, expected)

	def test_case_remove_punct2(self):
		text = "COVID-19"
		expected = "COVID-19"
		res = self.parser.remove_punct(text)
		self.assertEqual(res, expected)

	def test_case_remove_punct3(self):
		text = ","
		expected = ""
		res = self.parser.remove_punct(text)
		self.assertEqual(res, expected)

	def test_case_is_number_1(self):
		text = "1000"
		expected = True
		res = self.parser.is_number(text)
		self.assertEqual(res, expected)

	def test_case_is_number_2(self):
		text = "1,000"
		expected = True
		res = self.parser.is_number(text)
		self.assertEqual(res, expected)

	def test_case_is_number_3(self):
		text = "123Me"
		expected = False
		res = self.parser.is_number(text)
		self.assertEqual(res, expected)

class TestEntityRetrieve(TestSentenceParser):
	"""docstring for TestEntityRetrieve"""
	def test_cases_1(self):
		for i in range(len(SENTENCES)):
			sentence = SENTENCES[i]
			expected = OUTPUTS[i]
			res = set(self.parser.retrieve_keywords(sentence))
			self.assertEqual(res, expected)
if __name__ == '__main__':
	unittest.main(verbosity=3, exit =True)
