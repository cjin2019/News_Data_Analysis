import unittest
from data_analysis.sentence_parser import SentenceParser

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

	def test_case_1(self):
		sentence = "Beijing braces for 2nd wave of COVID-19 infections"
		expected = {"Beijing", "COVID-19"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_2(self):
		sentence = "Video of man confronted by white couple for stenciling Black Lives Matter goes viral"
		expected = {"Black Lives Matter"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_3(self):
		sentence = "Deadly force not 'only option' in Atlanta shooting: Rep. Val Demings"
		expected = {"Atlanta", "Val Demings"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_4(self):
		sentence = "Fauci tells ABC's 'Powerhouse Politics' that attending rallies, protests is 'risky'"
		expected = {"Fauci", "ABC", "Powerhouse Politics"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_5(self):
		sentence = "John Bolton's book recounts chaos, turmoil in Trump White House"
		expected = {"John Bolton", "Trump White House"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_6(self):
		sentence = "Black Americans most likely to know a COVID victim"
		expected = {"Black Americans", "COVID"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_7(self):
		sentence = "Energy producer BP takes $17.5b hit, demand down"
		expected = {"BP"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_8(self):
		sentence = "'Not productive' to compare presidents, after Trump's Lincoln comparison: Carson"
		expected = {"Trump", "Lincoln", "Carson"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_9(self):
		sentence = "Supreme Court bans LGBT employment discrimination"
		expected = {"Supreme Court", "LGBT"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_10(self):
		sentence = "Father, son beat and stab 12-year-old boy together"
		expected = set()
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_11(self):
		sentence = "Wildfire danger in West, flooding rain in East"
		expected = {"West", "East"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_12(self):
		sentence = "The Latest: WHO notes 100,000 new virus cases daily"
		expected = {"WHO"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_13(self):
		sentence = "Justices reject Trump bid to void California sanctuary law"
		expected = {"Trump", "California"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_14(self):
		sentence = "Expert warns of 'Coronavirus Carmageddon' if returning workers avoid mass transit"
		expected = {"Coronavirus", "Carmageddon"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)
	
	def test_case_15(self):
		sentence = "Videos show man went from speaking of visiting mom's grave to being killed by police"
		expected = set()
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_16(self):
		sentence = "Timeline: Trump’s response to the coronavirus pandemic"
		expected = {"Trump", "coronavirus"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)	

	def test_case_17(self):
		sentence = "A silver-lining from quarantine: A renewed bond between fathers and children"
		expected = set()
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_18(self):
		sentence = "Luke Bryan says his fans keep him grounded amid fame: 'I've always listened to what they had to say'"
		expected = {"Luke Bryan"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_19(self):
		sentence = "Thomas, Kavanaugh rip 'decade-long failure to protect Second Amendment'"
		expected = {"Thomas", "Kavanaugh", "Second Amendment"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_20(self):
		sentence = "Burgess Owens on NFL protests: 'It's about the flag, period!'"
		expected = {"Burgess Owens", "NFL"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_21(self):
		sentence = "There could be more than 30 alien civilizations in the Milky Way, shocking study says"
		expected = {"Milky Way"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_22(self):
		sentence = "Mom takes maternity pics at Chipotle, calls chain 'saving grace' during pregnancy"
		expected = {"Chipotle"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_23(self):
		sentence = "Twitter responds to Band-Aid's new bandages for diverse skin tones: 'Took long enough'"
		expected = {"Twitter", "Band-Aid"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_24(self):
		sentence = "GRAPHIC: Resurfaced blackface sketch, N-word use has Stern on ropes"
		expected = {"N-word", "Stern"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_24_b(self):
		sentence = "PHOTOS: Death of George Floyd sparks widespread outcry, protests"
		expected = {"George Floyd"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_25(self):
		sentence = "Twins sisters become valedictorian and salutatorian at same high school"
		expected = set()
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_26(self):
		sentence = "Planning to visit a national park? Here's what to know about reopening"
		expected = set()
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_27(self):
		sentence = "Slideshow of George Floyd Murals Around The World"
		expected = {"George Floyd Murals"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_28(self):
		sentence = "Maskless woman at NYC bagel shop intentionally coughs on patron who calls her out"
		expected = {"NYC"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_29(self):
		sentence = "Philadelphia's Tomb of the Unknown Soldier statue defaced with graffiti: 'Committed GENOCIDE'"
		expected = {"Philadelphia", "Tomb of the Unknown Soldier"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_30(self):
		sentence = "Dr. Siegel on uptick in coronavirus cases: Increased testing is 'not the whole story'"
		expected = {"Siegel", "coronavirus"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)

	def test_case_31(self):
		sentence = "Customer pranks rude driver in McDonald's drive-thru: 'Plot twist'"
		expected = {"McDonald"}
		res = set(self.parser.retrieve_keywords(sentence))
		self.assertEqual(res, expected)		

if __name__ == '__main__':
	unittest.main(verbosity=3, exit =True)
