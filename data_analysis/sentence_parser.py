import nltk
import spacy
import re

from data_analysis.word_sets import PROPER_NOUNS, COMMON_NOUNS
from data_analysis.sentence_cleaner import SentenceCleaner

class SentenceParser():
	"""docstring for SentenceParser"""
	
	def __init__(self):
		"""
		Initialized RegexpParser
		"""
		self.spacy_model = spacy.load("en_core_web_sm")
		self.sentence_cleaner = SentenceCleaner()

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
				cleaned_text = self.sentence_cleaner.clean_entity_text(text)
				if len(cleaned_text)>0:
					ents.append((cleaned_text, label))
				words_in_ents = words_in_ents | set(cleaned_text.split(" "))

		print("Parser", ents)
		ents1 = set(ents)
		ents2 = set(self.sentence_cleaner.retrieve_entities_not_caught(words_in_ents, sentence))
		return list(ents1 | ents2)

	def retrieve_keywords(self, sentence):
		"""
		Returns the list of entity text
		"""
		return [ent[0] for ent in self.retrieve_entities(sentence)]