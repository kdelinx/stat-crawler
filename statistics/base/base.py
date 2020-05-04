from scrapy.spiders import CrawlSpider

from requester import Requester


class BaseSpider(CrawlSpider):
    name = None

    def __init__(self, spider, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.spider = spider
        self.params = self.get_params(**kwargs)
        self.request_limit = self.get_request_limit()
        self.requester = Requester(self.request_limit)

    def get_params(self, **kwargs):
        """
        Return some params from db. It's can be called in other methods as self.params
        :param kwargs:
        :return:
        """
        return kwargs.copy()

    def get_request_limit(self):
        """
        Request per second limit
        :return: int limit or None
        """
        return 0
