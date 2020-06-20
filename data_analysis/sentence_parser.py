import nltk
import spacy
import re

from data_analysis.word_sets import PROPER_NOUNS
from data_analysis.word_sets import COMMON_NOUNS

class SentenceParser():
	"""docstring for SentenceParser"""
	
	def __init__(self):
		"""
		Initialized RegexpParser
		"""
		self.spacy_model = spacy.load("en_core_web_sm")
		self.word_set = set(nltk.corpus.words.words()) | COMMON_NOUNS
		self.wn = nltk.corpus.wordnet

	def part_of_speech_tag(self, sentence):
		"""
		Returns a list of tuples (part of speech, word)
		"""
		tokenized = nltk.word_tokenize(sentence)
		return nltk.pos_tag(tokenized)

	def chunk_noun_phrases(self, sentence):
		"""
		Returns a list of noun phrases
		"""
		grammar = "NP: {<PRP.?>?<CD>*<JJ.?>*<NN.*>*}"
		parser = nltk.RegexpParser(grammar)
		pos_tag = self.part_of_speech_tag(sentence)
		print()
		print("Sentence:", sentence)
		print("Part of speech:", pos_tag)
		chunks = parser.parse(pos_tag)

		noun_phrases = []
		for chunk in chunks:
			if type(chunk)!=tuple:
				noun_phrase_str = ''
				for (word, pos) in chunk.leaves():
					noun_phrase_str+=(word + ' ')
				noun_phrases.append(noun_phrase_str[:-1])
		return noun_phrases

	def in_restricted_entity(self, label):
		"""
		Returns whether the label is in restricted entity
		"""
		restricted = {"DATE", "TIME", "ORDINAL", "CARDINAL", "PERCENT", 
							"MONEY", "QUANTITY"}
		return label in restricted

	def has_number_tag(self, label):
		"""
		Returns whether the label refers to a quantity
		"""
		quantity_set = {"PERCENT", "MONEY"}
		return label in quantity_set

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

	def remove_punct(self, text):
		"""
		Returns the word without quotation or other punctuation
		"""
		if len(text) >=2 and text[-2:]=="'s":
			text = text[:-2]
		pattern = "([^\w\s-])"
		return re.sub(pattern, "", text)

	def get_base_form(self, word):
		"""
		Returns the base form of a word
		"""
		lower = word.lower()
		morphed = self.wn.morphy(lower)
		return word if morphed is None else morphed

	def is_proper_noun(self, word):
		"""
		Returns whether the word is a proper noun
		"""
		if word.isupper():
			return True
		if word in PROPER_NOUNS:
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
		return len(word)>0 and word not in words_in_ents and \
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
		return ents

	def retrieve_entities(self, sentence):
		"""
		Returns a list of people, organizations, countries, etc.
		Each item is a tuple (text, label)
		"""
		ents = []
		words_in_ents = set()

		for ent in self.spacy_model(sentence).ents:
			text, label = ent.text, ent.label_
			if not self.in_restricted_entity(label):
				cleaned_text = self.remove_punct(text)
				ents.append((cleaned_text, label))
				words_in_ents = words_in_ents | set(cleaned_text.split(" "))

		return ents + self.retrieve_entities_not_caught(words_in_ents, sentence)

	def retrieve_keywords(self, sentence):
		"""
		Returns the list of entity text
		"""
		return [ent[0] for ent in self.retrieve_entities(sentence)]