from rake_nltk import Metric, Rake

class KeywordRetriever(object):
	"""docstring for KeywordRetriever"""
	def __init__(self, min_length = 2, max_length = 4):
		"""
		Intializes Rake object
		"""
		self.rake = Rake(ranking_metric=Metric.WORD_DEGREE,max_length=max_length)

	def get_keywords(self, sentences):
		"""
		outputs the list of keywords from a list of sentences
		"""
		text = " ".join(sentences)
		self.rake.extract_keywords_from_text(text)
		return self.rake.get_ranked_phrases()

