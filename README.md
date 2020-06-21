# News_Data_Analysis
Analyze news content from different media

## How to Install/Setup
1. Install Python 3.7+
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: 
    1. windows: `venv/Scripts/activate`
    2. macOS: `source venv/bin/activate`
4. Install requirements: `pip install -r requirements.txt`
5. MySQL Setup:
    1. Install MySQL Server and MySQL Connector for python:
        1. windows: https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html
        2. macOS: https://dev.mysql.com/doc/refman/8.0/en/osx-installation.html
        3. linux: https://dev.mysql.com/doc/refman/8.0/en/linux-installation.html
    2. Create `config.py`. See `config.example.py` template for what values to put in `config.py`.
    3. (For MySQL Server) Create database: `python create_database.py`
    4. Connect to MySQL:

## How to Run

Project not finished! Instructions will be available when project is completed.

## Scrape Website
This project contains a script to scrape headlines from one of the following websites.
- https://abcnews.go.com/
- https://www.cnn.com/
- https://www.foxnews.com/
- https://www.nbcnews.com/
- https://www.reuters.com/

### How to Install
1. `python -m venv venv` 
2. Activate virtual environment: 
    1. windows: `venv/Scripts/activate`
    2. macOS: `source venv/bin/activate`
3. `pip install -r requirements.txt`

### How to Run
`python general_scrape.py`

## JS Scrape
This project contains a javascript script to scrape headlines from one of the following websites.
- https://www.foxnews.com/

Note: This script may be outdated. We recommend you use the python script to scrape websites.

### How to Install
1. install npm, node
2. `cd repository`
3. `npm install cheerio axios`

### How to Run
1. `cd scrape_web`
2. `node scrape_web/scrape1.js`

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

Description of our process:
1. Setup MySQL server (see Install section)
2. Used mysql-connector-python package to create database (see Install section)
3. Used mysql-connector-python package to insert headlines data into database

Resources that we used:
- https://www.edureka.co/blog/mysql-tutorial/
- https://www.cis.uni-muenchen.de/~hs/teach/14s/ir/rdbms.pdf
- https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html

### 3. Analyze data

Description of our process:
1. Used Natural Language Processing Modules: nltk
2.

Resources that we used:
- https://github.com/cjhutto/vaderSentiment#resources-and-dataset-descriptions

### 4. Automate gathering and storing data into database


