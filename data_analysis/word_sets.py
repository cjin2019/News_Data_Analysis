import nltk.corpus as nc

PROPER_NOUNS = {"Trump", "WHO", "coronavirus", "Twitter", "Stern"}

COMMON_NOUNS = set(nc.words.words()) | \
			   set(nc.stopwords.words('english')) | \
				{"timeline", "mom", "slideshow", "Dr"}