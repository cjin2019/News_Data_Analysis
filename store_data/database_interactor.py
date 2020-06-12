import mysql.connector 
from mysql.connector.cursor import MySQLCursor

class DatabaseInteractor:
	def __init__(self, username, password = None):
		"""
		Connects to the user for mysql 
		"""
		self.connector = mysql.connector.connect(user = username, password = password)
		self.cursor = MySQLCursor(self.connector)
	def create_database(self, db_name):
		"""
		Create a database (if it doesn't exist)
		"""
		create_db_cmd = 'CREATE DATABASE IF NOT EXISTS (%s)'
		params = (db_name,)
		self.cursor.execute(create_db_cmd, params)
	def close(self):
		"""
		Closes the connection once done
		"""
		self.connector.close()
		self.cursor.close()