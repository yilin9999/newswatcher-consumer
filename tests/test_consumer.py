from kafka_consumer.consumer_mongo.worker import NewsKafkaConsumerMongo
from kafka_consumer.consumer_rmdb.worker import NewsKafkaConsumerRMDB
# from kafka_consumer.app import init_rmdb
from kafka import KafkaConsumer
from .factories import MsgFactory
from .factories import MsgSample
# class MockConsumer(NewsKafkaConsumerRMDB):

#     class MockConsumerRecord():
#         msg = ""
#         offset = 0
#         value = ""

#     def __init__(self, record_list):
#         print("MockConsumer")
#         self.consumer = []
#         for i in range(len(record_list)):
#             self.consumer.append(self.MockConsumerRecord)


# class MockConsumerRMDB(NewsKafkaConsumerRMDB):

#     def __init__(self, msg_list=None):
#         self.offset = 0
#         if msg_list is None:
#             self.consumer = [MsgSample.sample1, MsgSample.sample2]
#         else:
#             self.consumer = msg_list

#     def run_consumer_batch(self):
#         while self.offset < len(self.consumer):
#             value = self.consumer[self.offset]
#             self.store_into_db(value)
#         return True

# class TestDB:
#     def test_init_rmdb(self):
#         init_rmdb()
#         print("Initialize RMDB")


class TestConsumer:

    def test_consumer_mongo(self):
        consumer_mongodb = NewsKafkaConsumerMongo()
        consumer_mongodb.run_consumer()

    def test_store_into_rmdb(self):
        self.consumer = [MsgSample.sample1, MsgSample.sample2]
        for value in self.consumer:
            NewsKafkaConsumerRMDB.store_into_db(value)

    def test_consumer_rmdb(self, mocker):
        # mocker.patch.object(NewsKafkaConsumerRMDB, "__init__", return_value=None)
        # mocker.patch.object(NewsKafkaConsumerRMDB, "run_consumer.msg", return_value=None)
        # KafkaMsgFactory()
        # mocker.patch.object(NewsKafkaConsumerRMDB, "run_consumer", side_effect=ttt)
        # mocker.patch.object("kafka_consumer.consumer_rmdb.worker.NewsKafkaConsumerRMDB", new_callable=MockConsumerRMDB)
        # consumer_rmdb = NewsKafkaConsumerRMDB()
        # consumer_rmdb.run_consumer()
        pass
