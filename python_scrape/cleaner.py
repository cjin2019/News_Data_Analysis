## This class cleans parsed data
##data: a list of  all the link titles
##exclude News category links/other links that are not news articles
class Cleaner:
	def __init__(self, link_list):
		self.link_list = link_list
	