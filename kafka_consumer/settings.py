import os
from dotenv import load_dotenv

load_dotenv()
curr_stage = os.getenv('STAGE', default=None)


class Config(object):
    TEST = ''
    CONSUMER_TIMEOUT_MS = 10000


class ProdConfig(Config):
    STAGE = 'production'
    KAFKA_BOOTSTRAP_SERVER = ''
    KAFKA_TOPIC_NEWS = ''
    MONGO_URI = ''


class DevConfig(Config):
    KAFKA_BOOTSTRAP_SERVER = 'localhost:9092'
    KAFKA_TOPIC_NEWS = 'test_mongodb'
    MONGO_URI = 'mongodb://david:newsgogogo@localhost:27017/newswatcher'
    # DBNAME = 'newswatcher'
    # MONGODB_SETTINGS = {
    #     'db': 'newswatcher',
    #     'host': 'mongodb://localhost:27017/newswatcher'
    #     # 'host': 'localhost',
    #     # 'port': 27017,
    #     # 'username': 'david',
    #     # 'password': 'newsgogogo'
    # }


if curr_stage == 'production':
    AppConfig = ProdConfig
else:
    AppConfig = DevConfig