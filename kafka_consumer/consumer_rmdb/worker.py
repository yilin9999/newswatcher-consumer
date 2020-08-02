import logging
import json
from kafka_consumer.consumer import NewsKafkaConsumer
from .database import NewsModel

logger = logging.getLogger(__name__)


class NewsKafkaConsumerRMDB(NewsKafkaConsumer):

    def __init__(self):
        super().__init__(group_id='rmdb')

    @classmethod
    def store_into_db(cls, data):
        news_inc = 0
        try:
            newsModel = NewsModel()
            newsModel.insert_news(data)
            logging.info("insert {} news".format(news_inc))
        except Exception as e:
            logging.error(str(e))
