import json
from kafka_consumer.settings import AppConfig
from kafka import KafkaProducer


class MsgFactory(object):
    topic = AppConfig.KAFKA_TOPIC_NEWS

    def __init__(self, sample_list=None, int_test=False):
        self._offset = 0
        if sample_list is None:
            self.msg_list = [default_sample_1, default_sample_2]
        else:
            self.msg_list = sample_list

    @property
    def offset(self):
        return self._offset


class KafkaMsgFactory(MsgFactory):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kafka_producer = KafkaProducer(
                                    bootstrap_servers=AppConfig.KAFKA_BOOTSTRAP_SERVER,
                                    value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        for msg in self.msg_list:
            self.kafka_producer.send(KafkaMsgFactory.topic, msg["data"])


class MsgSample:
    sample1 = {
        "time_elapsed": 4.51,
        "data_cnt": 2,
        "data": [
            {
                "title": "4遊客闖「平溪線隧道」！亮光一閃…駕駛員急煞：別拖我當劊子手",
                "media": "ETtoday",
                "date": "4 週前",
                "desc": "關於ETtoday. 電腦版 | 關於我們 · 聯絡信箱 | App下載. 東森新媒體控股股份有限公司版權所有 非經授權，不許轉載本網站內容 © ETtoday.net All Rights Reserved. 開.",
                "link": "https://www.ettoday.net/news/20200704/1752850.htm",
                "img": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw\u003d\u003d"
            },
            {
                "title": "隔離期落跑！24歲妹百貨公司爽吃拉麵 突接「確診電話」204人GG了",
                "media": "ETtoday",
                "date": "4 週前",
                "desc": "關於ETtoday. 電腦版 | 關於我們 · 聯絡信箱 | App下載. 東森新媒體控股股份有限公司版權所有 非經授權，不許轉載本網站內容 © ETtoday.net All Rights Reserved. 開.",
                "link": "https://www.ettoday.net/news/20200704/1752484.htm",
                "img": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw\u003d\u003d"
            }
        ]
    }
    sample2 = {
        "time_elapsed": 4.51,
        "data_cnt": 1,
        "data": [
            {
                "title": "中職／交易胡金龍？ 富邦採取開放態度",
                "media": "ETtoday",
                "date": "4 週前",
                "desc": "電腦版 | 關於我們. 東森新媒體控股股份有限公司版權所有 © ETtoday.net All Rights Reserved. ETtoday運動雲. \u003e 棒球. ETtoday運動雲. GO. 首頁 新聞快訊 棒球 籃球 ...",
                "link": "https://sports.ettoday.net/news/1752758",
                "img": "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw\u003d\u003d"
            }
        ]
    }
