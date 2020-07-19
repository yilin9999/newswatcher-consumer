import logging
import json
import sys
from kafka_consumer.settings import AppConfig
from kafka import KafkaConsumer

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class NewsKafkaConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
                            bootstrap_servers=AppConfig.KAFKA_BOOTSTRAP_SERVER,
                            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                            # auto_offset_reset='earliest',
                            consumer_timeout_ms=AppConfig.CONSUMER_TIMEOUT_MS)
        self.consumer.subscribe([AppConfig.KAFKA_TOPIC_NEWS])
