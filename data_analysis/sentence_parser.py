import nltk
import spacy

class SentenceParser():
	"""docstring for SentenceParser"""
	
	def __init__(self):
		"""
		Initialized RegexpParser
		"""
		self.pos_tag_model = spacy.load("en_core_web_sm")

	def part_of_speech_tag(self, sentence):
		"""
		Returns a list of tuples (part of speech, word)
		"""
		doc = self.pos_tag_model(sentence)
		return [(token.text, token.tag_) for token in doc]

	def chunk_noun_phrases(self, sentence):
		"""
		Returns a list of noun phrases
		"""
		grammar = "NP: {<PRP.?>?<JJ.?>*<NN.*>*}"
		parser = nltk.RegexpParser(grammar)
		pos_tag = self.part_of_speech_tag(sentence)
		print(pos_tag)
		chunks = parser.parse(pos_tag)

		noun_phrases = []
		for chunk in chunks:
			if type(chunk)!=tuple:
				noun_phrase_str = ''
				for (word, pos) in chunk.leaves():
					noun_phrase_str+=(word + ' ')
				noun_phrases.append(noun_phrase_str[:-1])
		return noun_phrases

