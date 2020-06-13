from store_data.database_interactor import DatabaseInteractor
from store_data.constants import DATABASE_NAME

def create_database(database_interactor):
    database_interactor.create_database(DATABASE_NAME)

def create_tables(database_interactor):
    

if __name__ == '__main__':
    print('hello')