# -*- coding: utf-8 -*-

import scrapy

class PackageItem(scrapy.Item):
    description = scrapy.Field()
    name = scrapy.Field()
    home_page = scrapy.Field()
    pypi_url = scrapy.Field()