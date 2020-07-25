import fire
from kafka_consumer.app import init_sqlite_db  # noqa F401
from kafka_consumer.app import start_mongo_consumer  # noqa F401
from kafka_consumer.app import start_rmdb_consumer  # noqa F401


if __name__ == '__main__':
    fire.Fire()
