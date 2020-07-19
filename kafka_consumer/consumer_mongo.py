import logging
import json
from kafka import KafkaConsumer
from pymongo import MongoClient
from pymongo.errors import BulkWriteError
from kafka_consumer.settings import AppConfig
from .consumer import NewsKafkaConsumer

logger = logging.getLogger(__name__)

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
        mgdb.db[NewsMongoDoc.collection].insert_many(input_array_dict, ordered=ordered)

    @classmethod
    def count_doc(self, doc_filter={}):
        return mgdb.db[NewsMongoDoc.collection].count_documents(doc_filter)


class NewsKafkaConsumerMongoDB(NewsKafkaConsumer):

    # def __init__(self):
    #     super().__init__()
        # self.consumer.config['group_id'] = 'g_mongodb'

    def run_consumer(self):
        # logger.info("Start Consumer")
        while True:
            logger.info("Start reading...")
            for msg in self.consumer:

                print("consume [{topic}]:  offset: {offset}\n{value}".format(
                        topic=AppConfig.KAFKA_TOPIC_NEWS,
                        offset=msg.offset,
                        value=json.dumps(msg.value, indent=4, ensure_ascii=False)))
                data = msg.value["data"]
                self.store_into_mongo(data=data)

    def store_into_mongo(self, data):

        news_inc = 0
        try:
            news_init_cnt = NewsMongoDoc.count_doc()
            NewsMongoDoc.insert_many(data, ordered=False)
            news_inc = NewsMongoDoc.count_doc() - news_init_cnt
        except BulkWriteError as e:
            logging.error(str(e))
        except Exception as e:
            logging.error(str(e))

        logging.info("insert {} news".format(news_inc))
