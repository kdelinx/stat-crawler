# -*- coding: utf-8 -*-

# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

from kafka import KafkaProducer


class StatisticsPipeline:
    client_id = 'statistics_pipe'
    topic_name = 'crawler.topic.start'

    def __init__(self):
        self.producer = None

    @staticmethod
    def _get_kafka_servers(spider):
        return [
            f'{server}:9092' for server in
            spider.crawler.settings.get('KAFKA_HOSTS')
        ]

    def open_spider(self, spider):
        self.producer = KafkaProducer(
            client_id=self.client_id,
            bootstrap_servers=self._get_kafka_servers(spider),
            value_serializer=lambda msg: json.dumps(msg).encode('ascii')
        )

    def process_item(self, item, spider):
        self.producer.send(self.topic_name, dict(item))
        return item

    def close_item(self, item, spider):
        self.producer.close()
