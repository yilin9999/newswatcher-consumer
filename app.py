from kafka_consumer.consumer_mongo.worker import NewsKafkaConsumerMongo


if __name__ == '__main__':
    consumer_mongodb = NewsKafkaConsumerMongo()
    consumer_mongodb.run_consumer()
