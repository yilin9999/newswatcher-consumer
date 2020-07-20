import logging
from pymongo import MongoClient
from pymongo.errors import BulkWriteError
from kafka_consumer.settings import AppConfig

client = MongoClient(AppConfig.MONGO_URI)
mgdb = client['newswatcher']


class NewsMongoDoc:
    collection = 'news'

    def __repr__(self):
        return '<NewsMongoDoc title:{0}>'.format(self.title)

    @classmethod
    def insert_one(self, input_dict):
        mgdb.db[NewsMongoDoc.collection].insert_one(input_dict)

    @classmethod
    def insert_many(self, input_array_dict, ordered):
        try:
            mgdb.db[NewsMongoDoc.collection].insert_many(input_array_dict, ordered=ordered)
        except BulkWriteError as e:
            logging.error(str(e))

    @classmethod
    def count_doc(self, doc_filter={}):
        return mgdb.db[NewsMongoDoc.collection].count_documents(doc_filter)
