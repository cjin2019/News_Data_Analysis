NEWS_URLS = {
    'fox': 'https://www.foxnews.com/', 
    'nbc': 'https://www.nbcnews.com/',
    'cnn': 'https://www.cnn.com/',
    'abc': 'https://abcnews.go.com/',
    'reuters': 'https://www.reuters.com/'
}

headline_markers = {
	'fox': [],
	'nbc': [],
	'cnn': [],
	'abc': {
        'tag': 'a',

    },
	'reuters': {'class:', ['story_title', 'article_heading']}
}