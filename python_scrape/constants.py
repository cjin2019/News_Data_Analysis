NEWS_URLS = {
    'fox': 'https://www.foxnews.com/', 
    'nbc': 'https://www.nbcnews.com/',
    'cnn': 'https://www.cnn.com/',
    'abc': 'https://abcnews.go.com/',
    'reuters': 'https://www.reuters.com/'
}

HEADLINE_MARKERS = {
	'fox': {
        'extract': [
            'header.info-header > h2 > a'
        ],
        'decompose': [
            'section.collection.collection-section.full-episodes'
        ]
    },
	'nbc': {
		'extract':[
			'.headline___38PFH',
			'.a-la-carte__headline',
			'.bacon-cards-twobyone__header-link vilynx_disabled',
			'[class^=pancake__headline]',
            'script'
		]
	},
	'cnn': {
		'extract':[
			'script'
		]
	},
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

REMOVE_STRS = [
	'\\u003cstrong>',
    '\\u003c/strong>',
	'Top Photos of the Day'
]
