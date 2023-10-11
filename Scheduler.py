from DB_Object import DB_Object
import threading
import time

class Scheduler:
	def __init__(self, numObjects, files):
		self.lock = threading.Lock()
		self.available_objects = []

		for x in range(numObjects):
			self.available_objects.append(DB_Object())


		self.threads = []
		for x in range(len(files)):
			self.threads.append(threading.Thread(target=self.threadedMethod, 
				args=(files[x][0], files[x][1],)))

		for x in range(len(self.threads)):
			self.threads[x].start()

		for x in range(len(self.threads)):
			self.threads[x].join()

	def getObject(self):
		with self.lock:
			if self.available_objects:
				obj = self.available_objects.pop()
			else:
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
			output = fileName()

			#Add data validity checking
			addData(output)

			time.sleep(sleep_time)



temp = Scheduler(15)