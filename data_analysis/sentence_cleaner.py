import nltk
import re

from data_analysis.word_sets import PROPER_NOUNS, COMMON_NOUNS, COMMON_ENTITY_NOUNS

class SentenceCleaner(object):
	"""docstring for SentenceCleaner"""

	def __init__(self):
		self.word_set = COMMON_NOUNS
		self.wn = nltk.corpus.wordnet
		self.ps = nltk.stem.PorterStemmer()

	def is_common_word(self, word):
		"""
		Returns whether the word is in nltk word set
		"""
		if word in self.word_set:
			return True
		if word.lower() in self.word_set:
			return True
		if self.get_base_form(word) in self.word_set:
			return True
		return False

	def is_common_entity_text(self, word):
		"""
		Helper for clean entity word
		1. Determine if word is under common_entity_nouns
		"""

		if word in COMMON_ENTITY_NOUNS:
			return True
		if word.lower() in COMMON_ENTITY_NOUNS:
			return True
		if self.get_base_form(word) in COMMON_ENTITY_NOUNS:
			return True
		return False

	def clean_entity_text(self, text):
		"""
		Cleans the entity by removing unnecessary junk
		1. Removes punctuation and 's
		2. Removes lower case words tailing upper case words
		"""
		text1 = self.remove_punct(text)
		text2 = self.remove_lower_words(text1)
		return text2 if not self.is_common_entity_text(text2) else ""

	def remove_punct(self, text):
		"""
		Returns the word without quotation or other punctuation
		"""
		if len(text) >=2 and text[-2:]=="'s":
			text = text[:-2]
		pattern = "([^\w\s-])"
		return re.sub(pattern, "", text)

	def remove_lower_words(self, text):
		"""
		Removes lowercase words tailing the text
		"""
		pattern1 = "[A-Z0-9]+[a-z]*"
		words = re.findall(pattern1, text)

		if len(words)==0:
			return ""

		return text[text.find(words[0]):text.find(words[-1]) + len(words[-1])]

	def get_base_form(self, word):
		"""
		Returns the base form of a word
		"""
		lower = word.lower()
		morphed = self.ps.stem(lower)

		if len(morphed)>4 and morphed[-4:]=="less":
			return morphed[:-4]

		idx = lower.find(morphed)
		if idx >= 0 and idx + len(morphed)<len(lower):
			if lower[idx + len(morphed)]=="e":
				return morphed+"e"
			elif lower[idx + len(morphed)-1:]=="ied":
				return morphed[:-1]+"y"
				
		return word if morphed is None else morphed

	def is_proper_noun(self, word):
		"""
		Returns whether the word is a proper noun
		"""
		if word in PROPER_NOUNS:
			return True
		if word.isupper() and not self.is_common_word(word):
			return True
		if not self.is_common_word(word) and not word.islower():
			return True
		return False

	def is_number(self, word):
		"""
		Returns whether the word is actually a number
		"""
		pattern = "([^0-9,])"
		return re.sub(pattern, "", word)==word

	def helper_not_caught(self, word, words_in_ents):
		"""
		Returns whether the words should be added to ents
		"""
		return len(word)>1 and word not in words_in_ents and \
				self.is_proper_noun(word) and not self.is_number(word)

	def retrieve_entities_not_caught(self, words_in_ents, sentence):
		"""
		Returns a list of entities that should have been added but 
		was not identified by spacy
		"""
		ents = []
		tokenized = nltk.word_tokenize(sentence)

		for word in tokenized:
			cleaned_word = self.remove_punct(word)
			if self.helper_not_caught(cleaned_word, words_in_ents):
				ents.append((cleaned_word, "UNLABELED"))

		#print("Cleaner:", ents)
		return ents

