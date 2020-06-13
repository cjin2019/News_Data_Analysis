import mysql.connector 
from mysql.connector import errorcode

class DatabaseInteractor:
    def __init__(self, username, password=None):
        """
		Connects to the user for mysql 
		"""
        self.connector = mysql.connector.connect(
			user=username, 
			password=password, 
			buffered=True
		)
        self.cursor = self.connector.cursor(self.connector)

    def create_database(self, db_name):
        """
    	Create a database (if it doesn't exist)
    	"""
        create_db_cmd = 'CREATE DATABASE IF NOT EXISTS {db_name}'
        try:
            self.cursor.execute(create_db_cmd)
            self.connector.database = db_name
        except mysql.connector.Error as err:
			print(f'Error occurred: {err}')
            print('Failed to create database')

    def choose_database(self, db_name):
        """
        Switch to database with db_name
        """
        use_db_cmd = f'USE {db_name}'
        try:
            self.cursor.execute(use_db_cmd)
        except mysql.connector.Error as err:
            print('Database does not exists')
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database(db_name)
                print ('Database created')
            else:
                print(err)

    def create_table(self, tble, db_name = None):
        """
        Create a table in the database (provided by self.connector 
        if db_name = None)
        """
        if db_name != None:
            self.choose_database(db_name)
        try:
            self.cursor.execute(tble)
            print('Created table in database')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table exists already")
            else:
                print(err)

    def close(self):
        """
		Closes the connection once done. Please add this execution to ensure 
        connections are closed!
		"""
        self.connector.close()
        self.cursor.close()
