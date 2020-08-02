from kafka_consumer.settings import AppConfig
from kafka_consumer.consumer_rmdb.database import BasicRMDB
from kafka_consumer.consumer_mongo.worker import NewsKafkaConsumerMongo
from kafka_consumer.consumer_rmdb.worker import NewsKafkaConsumerRMDB


def init_rmdb():

    basic_rmdb = BasicRMDB()
    basic_rmdb.init_rmdb()


def start_mongo_consumer():
    consumer_mongodb = NewsKafkaConsumerMongo()
    consumer_mongodb.run_consumer()


def start_rmdb_consumer():
    consumer_mongodb = NewsKafkaConsumerRMDB()
    consumer_mongodb.run_consumer()
