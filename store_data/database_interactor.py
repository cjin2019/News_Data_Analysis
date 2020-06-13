import mysql.connector 
from mysql.connector import errorcode
class DatabaseInteractor:
    def __init__(self, username, password = None):
        """
		Connects to the user for mysql 
		"""
        self.connector = mysql.connector.connect(user = username, password = password, buffered = True)
        self.cursor = self.connector.cursor(self.connector)

    def create_database(self, db_name):
        """
    	Create a database (if it doesn't exist)
    	"""
        create_db_cmd = f'CREATE DATABASE IF NOT EXISTS {db_name}'
        try:
            self.cursor.execute(create_db_cmd)
            self.connector.database = db_name
        except mysql.connector.Error as err:
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
        tble is a sql command
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

    def retrieve_columns(self, tble_name):
        """
        Retrieves the columns from tble_name
        Returns a list of tuples (column name, type, null, 
        whether it is the primary key, default value, extra)
        """
        show_tbl_stmt = f'SHOW COLUMNS FROM {tble_name}'
        try:
            self.cursor.execute(show_tbl_stmt)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print('Retrieve Table Error')

    def change_one_sql_command(self, sql_command):
        """
        SQL command that changes the database/table
        """
        try:
            self.cursor.execute(sql_command)
            self.connector.commit()
        except mysql.connector.Error as err:
            print('Error in executing change command')

    def fetch_one_sql_command(self, sql_command):
        """
        SQL command that fetches values 
        Returns a list of tuple if there are results
        Otherwise, an empty list if there are none
        """
        try:
            self.cursor.execute(sql_command)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print('Error in fetching')

    def insert_one_row(self, tble_name, datum):
        """
        Inserts into table the corresponding datum
        Takes in datum: a tuple following the order of the columns in 
        the table

        Possible Errors: datum is wrong length, the datatype is incorrect, etc
        """
        ncols = len(self.retrieve_columns(tble_name))
        input_format = '(' + '%s,' * (ncols-1) + '%s' + ')'
        insert_stmt = f'INSERT INTO {tble_name} VALUES {input_format}'

        try:
            self.cursor.execute(insert_stmt, datum)
            self.connector.commit()                                 #makes sure the changes are actually made to table
        except mysql.connector.Error as err:
            print('Insertion Error')

    def insert_many_rows(self, tble_name, data):
        """
        Insert into table many rows from data
        Takes in data: a list of tuples
        """
        ncols = len(self.retrieve_columns(tble_name))
        input_format = '(' + '%s,' * (ncols-1) + '%s' + ')'
        insert_many_stmt = f'INSERT INTO {tble_name} VALUES {input_format}'

        try:
            self.cursor.executemany(insert_many_stmt, data)
            self.connector.commit()
        except mysql.connector.Error as err:
            print('Inserting many Error')

    def close(self):
        """
		Closes the connection once done. Please add this execution to ensure 
        connections are closed!
		"""
        self.connector.close()
        self.cursor.close()