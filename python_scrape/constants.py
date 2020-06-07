NEWS_URLS = {
    'fox': 'https://www.foxnews.com/', 
    'nbc': 'https://www.nbcnews.com/',
    'cnn': 'https://www.cnn.com/',
    'abc': 'https://abcnews.go.com/',
    'reuters': 'https://www.reuters.com/'
}

HEADLINE_MARKERS = {
	'fox': [],
	'nbc': [],
	'cnn': [],
	'abc': {
        'extract': {},
        'decompose': [
            'nav',
            'article._footer',
            'a.video-modal',
            'span.duration',
            'div.container',
            'div.live-callout'
        ]
    },
	'reuters': {'class': ['story_title', 'article_heading']}
}