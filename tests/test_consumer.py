from kafka_consumer.consumer_mongo import NewsKafkaConsumerMongoDB


class TestConsumer:

    def test_basic(self):
        consumer_mongodb = NewsKafkaConsumerMongoDB()
        consumer_mongodb.run_consumer()
