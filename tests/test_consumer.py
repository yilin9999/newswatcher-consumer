from kafka_consumer.consumer_mongo.worker import NewsKafkaConsumerMongo


class TestConsumer:

    def test_basic(self):
        consumer_mongodb = NewsKafkaConsumerMongo()
        consumer_mongodb.run_consumer()
