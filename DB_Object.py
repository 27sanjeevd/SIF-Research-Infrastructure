import mysql.connector

class DB_Object:
	def __init__(self):
		"""
		Code that establishes a connection to the db (currently mysql, but later aws/azure)
		"""
		self.cnx = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database_name"
        )

	def store_data(self, sql_statement, vals):
		mycursor = self.cnx.cursor()

		mycursor.execute(sql, val)
		self.cnx.commit()

