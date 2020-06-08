NEWS_URLS = {
    'fox': 'https://www.foxnews.com/', 
    'nbc': 'https://www.nbcnews.com/',
    'cnn': 'https://www.cnn.com/',
    'abc': 'https://abcnews.go.com/',
    'reuters': 'https://www.reuters.com/'
}

HEADLINE_MARKERS = {
	'fox': [],
	'nbc': {
		'extract':[
			'.headline___38PFH',
			'.a-la-carte__headline',
			'.bacon-cards-twobyone__header-link vilynx_disabled',
			'[class^=pancake__headline]'
		]
	},
	'cnn': [],
	'abc': {
        'extract': [
            'a'
        ],
        'decompose': [
            'nav',
            'article._footer',
            'a.video-modal',
            'span.duration',
            'div.container',
            'div.live-callout'
        ]
    },
	'reuters': {
		'extract': [
		'.story-title',
		'.article_heading']}
}