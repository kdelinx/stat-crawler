# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, Join


class RusprofileItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join(),
    )
    is_active_organization = scrapy.Field()
    ogrn = scrapy.Field()
    ogrn_date_from = scrapy.Field()
    date_register = scrapy.Field()
    law_address = scrapy.Field()
    owner = scrapy.Field()
    owner_date_from = scrapy.Field()
    inn_number = scrapy.Field()
    kpp_number = scrapy.Field()
    authorized_capital = scrapy.Field()
    primary_occupation = scrapy.Field()
    primary_occupation_code = scrapy.Field()
    tax_authority = scrapy.Field()
    tax_authority_date_from = scrapy.Field()
    okpo = scrapy.Field()
    okato = scrapy.Field()
    okogu = scrapy.Field()
    oktmo = scrapy.Field()


class FoundersRusprofileItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    is_liquidate = scrapy.Field()
    part_money = scrapy.Field()
    part_percentile = scrapy.Field()
    president_commission = scrapy.Field()
    law_address = scrapy.Field()
    inn = scrapy.Field()
    ogrn = scrapy.Field()
    date_register = scrapy.Field()


class FinancesRusprofileItem(scrapy.Item):
    ...
