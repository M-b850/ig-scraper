from pymongo import MongoClient

# Change the link if you're using diffrent database
db_address = "mongodb://admin:password@localhost:8080/admin?authSource=admin"

class DB:

	def __init__(self):
		self.client = None
		self.col = None

	def connect(self):
		""" Get connected to database. """
		self.client = MongoClient(db_address)
		if self.client: print('~~~ Connected. ~~~\n')

	def select_database(self, db_name):
		""" Select database. """
		self.db = self.client[db_name]
		return self.db

	def comments_col(self):
		""" Select default collection as comments. """
		self.col = self.db.comments
		return self.col

	def posts_col(self):
		""" Select default collection as posts. """
		self.col = self.db.posts
		return self.col

	def refinstagram_col(self):
		""" Select default collection as refinstagram. """
		self.col = self.db.refinstagram
		return self.col

	def insert_one(self, doc):
		""" Insert into selected collection. """
		obj = self.col.insert_one(doc)
		return obj

	def find_one(self, filter):
		""" Find in selected collection. """
		return self.col.find_one(filter)

	def get_databases(self):
		""" Get list of databases. """
		dbs = self.client.list_database_names()
		return dbs
	
	def delete_one(self, filter):
		""" Delete selected document from database. """
		return self.col.delete_one(filter)

	def find_delete(self, filter):
		""" Find and delete document by filter. """
		return self.col.find_one_and_delete(filter)

	def save(self, doc):
		return self.col.save(doc)
