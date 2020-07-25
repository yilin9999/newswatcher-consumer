from kafka_consumer.consumer_mongo.worker import NewsKafkaConsumerMongo
from kafka_consumer.consumer_rmdb.worker import NewsKafkaConsumerRMDB


class TestConsumer:

    def test_consumer_mongo(self):
        consumer_mongodb = NewsKafkaConsumerMongo()
        consumer_mongodb.run_consumer()

    def test_consumer_rmdb(self):
        consumer_mongodb = NewsKafkaConsumerRMDB()
        consumer_mongodb.run_consumer()
