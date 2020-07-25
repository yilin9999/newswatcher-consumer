import logging
import json
from kafka_consumer.settings import AppConfig
from kafka_consumer.consumer import NewsKafkaConsumer
from .docs import NewsMongoDoc

logger = logging.getLogger(__name__)


class NewsKafkaConsumerMongo(NewsKafkaConsumer):

    def __init__(self):
        super().__init__(group_id='mongo')

    def store_into_db(self, data):

        news_inc = 0
        try:
            news_init_cnt = NewsMongoDoc.count_doc()
            NewsMongoDoc.insert_many(data, ordered=False)
            news_inc = NewsMongoDoc.count_doc() - news_init_cnt
        except Exception as e:
            logging.error(str(e))

        logging.info("insert {} news".format(news_inc))
