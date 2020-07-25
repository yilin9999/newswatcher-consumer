import logging
import json
import sys
from abc import ABCMeta, abstractmethod
from kafka_consumer.settings import AppConfig
from kafka import KafkaConsumer

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class NewsKafkaConsumer(metaclass=ABCMeta):
    def __init__(self, group_id=None):
        self.consumer = KafkaConsumer(
                            bootstrap_servers=AppConfig.KAFKA_BOOTSTRAP_SERVER,
                            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                            group_id=group_id,
                            auto_offset_reset='earliest',
                            consumer_timeout_ms=AppConfig.CONSUMER_TIMEOUT_MS)
        self.consumer.subscribe([AppConfig.KAFKA_TOPIC_NEWS])

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
                self.store_into_db(data=data)

    @abstractmethod
    def store_into_db(self, data):
        pass
