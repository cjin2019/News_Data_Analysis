from nltk.corpus import opinion_lexicon
from nltk.tokenize import treebank
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentAnalyzer:

	def liu_and_hu_polarity(self, sentence):
		"""
		Uses the list of positive and negative words
		compiled by Liu and Hu to determine if the sentence
		leans to positive, negative or neutral

		Returns pos_word ratio - neg_word ratio
		> 0 --> positive
		< 0 --> negative
		"""
		tokenizer = treebank.TreebankWordTokenizer()
		pos_words = 0
		neg_words = 0
		tokenized_sent = [word.lower() for word in tokenizer.tokenize(sentence)]

		for word in tokenized_sent:
			if word in opinion_lexicon.positive():
				pos_words+=1
			elif word in opinion_lexicon.negative():
				neg_words+=1
		
		total_words = len(tokenized_sent)
		return (pos_words - neg_words)/total_words

	def vader_polarity(self, sentence):
		"""
		Uses the VADER scoring metric to determine the polarity
		of the sentences
		"""
		analyzer = SentimentIntensityAnalyzer()
		return analyzer.polarity_scores(sentence)['compound']