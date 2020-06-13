##Note: need to create configuration file to access mysql
from store_data.database_interactor import DatabaseInteractor
from store_data.config import USER_INFO
from store_data.sql_table import TABLE_EX1

user = USER_INFO['user']
passwd = USER_INFO['password']
dbI = DatabaseInteractor(user, password = passwd)
#dbI.create_database('testDB2')
dbI.choose_database('testDB2')
dbI.create_table(TABLE_EX1)
dbI.close()

