DATABASE_NAME = 'NewsHeadlinesData'

CREATE_TABLES_CMDS = [
    'CREATE TABLE NewsSource \
    (Id INT NOT NULL AUTO_INCREMENT, \
    Name VARCHAR(255) NOT NULL, \
    Url VARCHAR(255) NOT NULL, \
    PRIMARY KEY (Id)) \
    ENGINE=INNODB;',
    'CREATE TABLE Headline \
    (Id INT AUTO_INCREMENT, \
    Content VARCHAR(255) NOT NULL, \
    Datetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, \
    PRIMARY KEY (Id)) \
    ENGINE=INNODB;',
    'CREATE TABLE NewsSourceHeadline \
    (Id INT AUTO_INCREMENT, \
    NewsSourceId INT NOT NULL, \
    HeadlineId INT NOT NULL, \
    PRIMARY KEY (Id), \
    FOREIGN KEY (NewsSourceId) \
        REFERENCES NewsSource(Id), \
    FOREIGN KEY (HeadlineId) \
        REFERENCES Headline(Id)) \
    ENGINE=INNODB;'
]

INSERT_CMDS = [
    'INSERT INTO NewsSource \
    (Name, Url) \
    VALUES \
    ("abc", "https://abcnews.go.com/"), \
    ("fox", "https://www.foxnews.com/"), \
    ("nbc", "https://www.nbcnews.com/"), \
    ("reuters", "https://www.reuters.com/");'
]