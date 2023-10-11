from DB_Object import DB_Object
import threading
import time

"""

Main things to work on:

1) in @threadedMethod, be able to run the file based on filename
2) in @DB_Object, connect to the db. make sure to use gitignore or env object

"""
class Scheduler:
	def __init__(self):
		self.lock = threading.Lock()
		self.available_objects = []
		self.threads = []
		

	def createDBObjects(self, numObjects):
		for x in range(numObjects):
			self.available_objects.append(DB_Object())

	def readFiles(self, files):
		for file_name, sleep_time in files:
			self.threads.append(threading.Thread(target=self.threadedMethod, 
				args=(file_name, sleep_time)))

		for thread in self.threads:
			thread.start()


	def getObject(self):
		check1 = False

		with self.lock:
			if self.available_objects:
				obj = self.available_objects.pop()
			else:
				check1 = True

		if check1:
			obj = DB_Object()

		return obj

	def returnObject(self, obj);
		with self.lock:
			self.available_objects.append(obj)

	def addData(self, data):
		db_object = self.getObject()
		db_object.store_data(data[0], data[1])

		self.returnObject(db_object)


	def threadedMethod(self, fileName, sleep_time):
		while True:
			table, labels, output = fileName()

			if (isinstance(labels, list) and isinstance(output, list) 
				and len(labels) == len(output)):

				statement = f"INSERT INTO {table} ({', '.join(labels)}) VALUES ({', '.join(['%s' for _ in labels])})"
				vals = tuple(output)

				addData(statement, vals)

			time.sleep(sleep_time)

