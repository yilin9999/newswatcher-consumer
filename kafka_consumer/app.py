from kafka_consumer.settings import AppConfig
from kafka_consumer.consumer_rmdb.database import BasicRMDB
from kafka_consumer.consumer_mongo.worker import NewsKafkaConsumerMongo
from kafka_consumer.consumer_rmdb.worker import NewsKafkaConsumerRMDB


def init_sqlite_db():

    basic_rmdb = BasicRMDB(AppConfig.RMDB_URL)
    basic_rmdb.init_sqlite_db()


def start_mongo_consumer():
    consumer_mongodb = NewsKafkaConsumerMongo()
    consumer_mongodb.run_consumer()


def start_rmdb_consumer():
    consumer_mongodb = NewsKafkaConsumerRMDB()
    consumer_mongodb.run_consumer()
