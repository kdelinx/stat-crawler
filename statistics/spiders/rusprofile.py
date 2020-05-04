# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader

from base.base import BaseSpider
from ..items import (
    RusprofileItem,
)


class RusprofileSpider(BaseSpider):
    name = "rusprofile"
    load_item = RusprofileItem
    allowed_domains = ["rusprofile.ru"]
    start_urls = ["https://www.rusprofile.ru/"]
    rules = ()

    def parse(self, response):
        main_loader = ItemLoader(item=self.load_item(), response=response)
        main_loader.add_value()
        main_loader.add_xpath()

        return main_loader.load_item()
