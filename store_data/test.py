##Note: need to create configuration file to access mysql
from database_interactor import DatabaseInteractor
from config import USER_INFO
from sql_table import TABLE_EX1

user = USER_INFO['user']
passwd = USER_INFO['password']
dbI = DatabaseInteractor(user, password = passwd)
#dbI.create_database('testDB2')
dbI.choose_database('testDB2')
dbI.create_table(TABLE_EX1)
print(dbI.retrieve_columns('customers'))
#dbI.insert_one_row("customers", (1, "Alison", "125 Elm Street"))
data = [
	(2, 'Bridgit', '12 Kings Crossing'),
	(3, 'Calum', '38 Little Acorn Street')
]
dbI.insert_many_rows('customers', data)
dbI.close()

