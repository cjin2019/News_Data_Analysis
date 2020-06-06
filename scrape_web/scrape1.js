const cheerio = require('cheerio');
const axios = require('axios');
const fs = require('fs');

axios.get('https://www.foxnews.com/').then((response) =>{
	const $ = cheerio.load(response.data);
	let altElems = [];
	$('img').each(function (i, e){
		altElems[i] = $(this).attr('alt');
	})
	fs.writeFile('output.txt', altElems, (error) => { });
})
