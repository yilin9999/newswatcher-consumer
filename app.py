from kafka_consumer.consumer_mongo import NewsKafkaConsumerMongoDB


if __name__ == '__main__':
    consumer_mongodb = NewsKafkaConsumerMongoDB()
    consumer_mongodb.run_consumer()

