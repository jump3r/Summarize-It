import time
import datetime
import pymongo


MONGODB_URI = 'mongodb://uftshuttlebus:uftshuttle@ds048537.mongolab.com:48537/mongo_db1' 
#if 'RUN_LOCAL' in os.environ and os.environ['RUN_LOCAL'] == 'yes':
#	MONGODB_URI = 'mongodb://localhost:27017'
DEFAULT_DB = 'mongo_db1'


class QueryDAO:

	@staticmethod
	def SaveQuerySource(uri):
		client = pymongo.MongoClient(MONGODB_URI)
		db = client[DEFAULT_DB]
		
		collection = db['sumit_uri_s']

		collection.insert({ "time": datetime.datetime.utcnow(), "uri": uri })

		client.close()


	@staticmethod
	def GetQuerySources():
		client = pymongo.MongoClient(MONGODB_URI)
		db = client[DEFAULT_DB]
		
		collection = db['sumit_uri_s']

		records = collection.find()

		formatted = []
		#for rec in records:

		client.close()

		return formatted

