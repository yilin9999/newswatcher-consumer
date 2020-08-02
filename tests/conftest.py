import pytest
import os
from kafka_consumer.app import init_rmdb


@pytest.fixture(scope='function')
def clean_kafka_tests_topic():
    delete_cmd = 'docker exec -it kafka kafka-topics.sh --delete --bootstrap-server localhost:9092 --topic tests'
    os.system(delete_cmd)
