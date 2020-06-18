import spacy

class EntityRecognizer:
	"""docstring for EntityRecognizer"""
	def __init__(self):
		"""
		Intializes the model
		"""
		self.nlp = spacy.load("en_core_web_sm")
	
	def retrieve_entities(self, sentence):
		"""
		Returns a list of entities (text, entity type). 
		An entity is proper noun 
		"""
		return [(ent.text, ent.label_) for ent in self.nlp(sentence).ents]

