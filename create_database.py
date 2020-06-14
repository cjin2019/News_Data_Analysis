from store_data.database_interactor import DatabaseInteractor
from store_data.constants import DATABASE_NAME, CREATE_TABLES_CMDS
import config

def create_database(database_interactor):
    print('creating database')
    database_interactor.create_database(DATABASE_NAME)

def create_tables(database_interactor):
    print('creating tables')
    for cmd in CREATE_TABLES_CMDS:
        database_interactor.create_table(cmd)

def fill_news_outlet_table(database_interactor):
    print('filling news_outlet_table')

if __name__ == '__main__':
    print('Starting to create database ...')
    database_interactor = DatabaseInteractor(
        config.username,
        config.password
    )
    create_database(database_interactor)
    create_tables(database_interactor)
    fill_news_outlet_table(database_interactor)
    database_interactor.close()
