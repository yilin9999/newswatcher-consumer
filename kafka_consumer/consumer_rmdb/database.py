import sqlite3
import os
import logging
from kafka_consumer.settings import AppConfig

logger = logging.getLogger(__name__)


class BasicRMDB():
    def __init__(self):
        self.conn = sqlite3.connect(AppConfig.RMDB_URL)

    def init_sqlite_db(self):
        with self.db as cursor:
            print(os.path.join(AppConfig.PROJECT_ROOT, "kafka_consumer/consumer_rmdb/schema.sql"))
            SQLITE_DB_PATH = os.path.join(AppConfig.PROJECT_ROOT, "kafka_consumer/consumer_rmdb/schema.sql")
            cursor.execute(open(SQLITE_DB_PATH, "r").read())


class NewsModel(BasicRMDB):

    def insert_news(self, data):
        c = self.conn.cursor()
        c.execute("")
        self.conn.commit()
        logger.info("Insert News")
