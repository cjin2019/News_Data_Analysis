# News_Data_Analysis
Analyze news content from different media

## How to Install
1. Install python 3.7+
2. Create virtual environment: python -m venv venv
3. Activate virtual environment: 
    (1) venv/Scripts/activate (windows)
    (2) source venv/bin/activate (mac)
4. Install requirements: pip install -r requirements.txt
5. Install mysql server: https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html

## How to Run

Project not finished! Instructions will be available when project is completed.

## Python scrape
This project contains a script to scrape headlines from one of the following websites.
- https://abcnews.go.com/
- https://www.cnn.com/
- https://www.foxnews.com/
- https://www.nbcnews.com/
- https://www.reuters.com/

### How to Install
1. python -m venv venv 
2. venv/Scripts/activate
3. pip install -r requirements.txt

### How to Run
1. cd python_scrape
2. python general_scrape.py

## JS Scrape
This project contains a javascript script to scrape headlines from one of the following websites.
- https://abcnews.go.com/
- https://www.cnn.com/
- https://www.foxnews.com/
- https://www.nbcnews.com/
- https://www.reuters.com/

Note: This script may be outdated. We recommend you use the python script to scrape websites.

### How to Install
1. install npm, node
2. cd repository
3. npm install cheerio axios

### How to Run
1. cd scrape_web
2. node scrape_web/scrape1.js

## Project Description

### 1. Scrape and clean data from website

Description of our process:
1. Grabbed html from a given website
2. Used BeautifulSoup package to parse html and find headlines

Resources that we used:
- https://www.dataquest.io/blog/web-scraping-tutorial-python/
- https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/#tag

### 2. Store data in database

Resources that we used:
https://www.postgresql.org/docs/12/tutorial.html
https://www.hostingadvice.com/how-to/free-postgresql-hosting/
https://www.edureka.co/blog/mysql-tutorial/
https://www.cis.uni-muenchen.de/~hs/teach/14s/ir/rdbms.pdf

