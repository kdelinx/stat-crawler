# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, Join, Compose

_prepare_law_address = lambda t: ' '.join(t).replace('\n', '.')


class RusprofileItem(scrapy.Item):
    id = scrapy.Field(output_processor=Join(), )
    title = scrapy.Field(output_processor=Join(), )
    is_active_organization = scrapy.Field(
        output_processor=Join(),
    )
    ogrn = scrapy.Field(output_processor=Join(), )
    ogrn_date_from = scrapy.Field(
        input_processor=MapCompose(), output_processor=Join(),
    )
    date_register = scrapy.Field(output_processor=Join(), )
    law_address = scrapy.Field(
        output_processor=Join(), input_processor=Compose(_prepare_law_address)
    )
    owner = scrapy.Field(output_processor=Join(), )
    owner_date_from = scrapy.Field(output_processor=Join(), )
    inn_number = scrapy.Field(output_processor=Join(), )
    kpp_number = scrapy.Field(output_processor=Join(), )
    authorized_capital = scrapy.Field(output_processor=Join(), )
    primary_occupation = scrapy.Field(output_processor=Join(), )
    primary_occupation_code = scrapy.Field(output_processor=Join(), )
    tax_authority = scrapy.Field(output_processor=Join(), )
    tax_authority_date_from = scrapy.Field(output_processor=Join(), )
    okpo = scrapy.Field(output_processor=Join(), )
    okato = scrapy.Field(output_processor=Join(), )
    okogu = scrapy.Field(output_processor=Join(), )
    oktmo = scrapy.Field(output_processor=Join(), )


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
