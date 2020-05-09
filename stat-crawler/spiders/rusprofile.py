# -*- coding: utf-8 -*-
from urllib.parse import urlparse

from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import Rule

from ..base.base import BaseSpider
from ..items import (
    RusprofileItem,
)


class RusprofileSpider(BaseSpider):
    name = "rusprofile"
    load_item = RusprofileItem
    allowed_domains = ["rusprofile.ru"]
    start_urls = ["https://www.rusprofile.ru/search?query=бетон&type=ul"]
    rules = (
        Rule(LinkExtractor(allow='id/'), callback='parse_item', follow=True),
    )

    # scrapy parse --spider=rusprofile -c parse_item https://www.rusprofile.ru/id/4260375

    def parse_item(self, response):
        _request_url = urlparse(response.url)
        main_loader = ItemLoader(item=self.load_item(), response=response)

        main_loader.add_value('id', _request_url.path.strip('/id/'))
        main_loader.add_xpath('title', '//*[@id="anketa"]/div[1]/div[1]/div[1]/text()')
        main_loader.add_xpath('is_active_organization', '//*[@id="anketa"]/div[1]/div[1]/div[2]/text()')
        main_loader.add_xpath('ogrn', '//*[@id="clip_ogrn"]/text()')
        main_loader.add_xpath('ogrn_date_from', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[1]/dl[1]/dd[2]/text()')
        main_loader.add_xpath('date_register', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd/text()')
        main_loader.add_xpath('law_address', '//*[@id="anketa"]/div[2]/div[1]/div[2]/address/span/text()')
        # main_loader.add_xpath('date_register', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd')
        # main_loader.add_xpath('date_register', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd')
        # main_loader.add_xpath('date_register', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd')
        # main_loader.add_xpath('date_register', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd')
        # main_loader.add_xpath('date_register', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd')
        # main_loader.add_xpath('date_register', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd')
        # main_loader.add_xpath('date_register', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd')
        # main_loader.add_xpath('date_register', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd')
        # main_loader.add_xpath('date_register', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd')
        # main_loader.add_xpath('date_register', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd')
        # main_loader.add_xpath('date_register', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd')
        # main_loader.add_xpath('date_register', '//*[@id="anketa"]/div[2]/div[1]/div[1]/div[2]/dl[1]/dd')

        yield main_loader.load_item()
