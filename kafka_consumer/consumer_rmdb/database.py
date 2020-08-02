from sqlalchemy import create_engine
from sqlalchemy import text
import os
import logging
from kafka_consumer.settings import AppConfig

logger = logging.getLogger(__name__)


class BasicRMDB():
    def __init__(self):
        DB_PATH = AppConfig.RMDB_URL
        if DB_PATH.startswith("sqlite:"):
            self.engine = create_engine(AppConfig.RMDB_URL)
        elif DB_PATH.startswith("postgresql:"):
            self.engine = create_engine(AppConfig.RMDB_URL,
                                        pool_size=10, pool_recycle=3600)
        else:
            raise(f"Cannot Support this DB engine: {AppConfig.RMDB_URL}")
        # escaped_sql = sqlalchemy.text(file.read())
        # result = self.conn.execute("select * from public.newsinfo")
        # for row in result:
        #     print(row)
        # pass

    def init_rmdb(self):
        conn = self.engine.connect()
        schema_path = os.path.join(AppConfig.PROJECT_ROOT, "kafka_consumer/consumer_rmdb/schema.sql")
        with open(schema_path, "r") as fptr:
            escaped_sql = text(fptr.read())

        conn.execute(escaped_sql)
        logging.info("Initalize DB successfully!!")
        # print(os.path.join(AppConfig.PROJECT_ROOT, "kafka_consumer/consumer_rmdb/schema.sql"))
        # SQLITE_DB_PATH = ""
        # cursor.execute(open(SQLITE_DB_PATH, "r").read())


class NewsModel(BasicRMDB):

    def insert_news(self, data):
        c = self.conn.cursor()
        c.execute("")
        self.conn.commit()
        logger.info("Insert News")
