"""
Sources:
1. https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html
"""

from store_data.database_interactor import DatabaseInteractor
from store_data.constants import DATABASE_NAME, CREATE_TABLES_CMDS, INSERT_CMDS
from config import USER_INFO

def create_database(database_interactor):
    print('creating database')
    database_interactor.create_database(DATABASE_NAME)

def create_tables(database_interactor):
    print('creating tables')
    for cmd in CREATE_TABLES_CMDS:
        database_interactor.create_table(cmd)

def fill_tables(database_interactor):
    print('inserting news source data into NewsSource')
    for cmd in INSERT_CMDS:
        database_interactor.change_one_sql_command(cmd)

if __name__ == '__main__':
    print('Starting to create database ...')
    database_interactor = DatabaseInteractor(
        USER_INFO['user'],
        USER_INFO['password']
    )
    create_database(database_interactor)
    create_tables(database_interactor)
    fill_tables(database_interactor)
    print('Finished! Closing database connector ...')
    database_interactor.close()
