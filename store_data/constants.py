DATABASE_NAME = 'news_headlines_data'

CREATE_TABLES_CMDS = [
    "CREATE TABLE news_source \
    (id INT AUTO_INCREMENT PRIMARY KEY, \
    name VARCHAR(255) NOT NULL, \
    url VARCHAR(255) NOT NULL)",
    "CREATE TABLE headline \
    (id INT AUTO_INCREMENT PRIMARY KEY, \
    content VARCHAR(255) NOT NULL, \
    datetime DATETIME NOT NULL)",
    "CREATE news_source_headline \
    (id INT AUTO_INCREMENT PRIMARY KEY, \
    news_source_id int FOREIGN KEY REFERENCES news_source(news_source_id}, \
    headline_id int FOREIGN KEY REFERENCES headline(headline_id))"
]