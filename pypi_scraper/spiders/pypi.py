# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.http.request import Request

from ..items import PackageItem

class PYPISpider(CrawlSpider):
    start_urls = ['https://pypi.python.org/pypi?:action=browse&show=all&c=483']
    name = "pypi"

    def parse(self, response):
        # parse table with packages
        table_rows = response.css('table.list tbody tr')
        for row in table_rows[1:5]: # ignore thead and get first 10 packages
            item = PackageItem()
            #item['description'] = row.css('td::text').extract() 
            #item['name'] = row.css('td a::text').extract()
            item['pypi_url'] = row.css('td a::attr(href)').extract()

            if item['pypi_url']:
                item['pypi_url'] = 'https://pypi.python.org%s' % item['pypi_url'][0]

            yield Request(
                item['pypi_url'],
                dont_filter=True,
                meta={'item': item},
                callback=self.parse_package
            )

    def parse_package(self, response):
        item = response.meta['item']
        home_page = response.xpath('//ul[@class="nodot"]/li/strong[contains(text(),"Home Page:")]/../a/@href').extract()
        item['home_page'] = home_page[0] if home_page else ''
        yield item
