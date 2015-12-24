# -*- coding: utf-8 -*-

BOT_NAME = 'pypi_scraper'

SPIDER_MODULES = ['pypi_scraper.spiders']
NEWSPIDER_MODULE = 'pypi_scraper.spiders'

CONCURRENT_REQUESTS = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1
AUTOTHROTTLE_ENABLED = True

USER_AGENT = """
    Mozilla/5.0 (Windows NT 6.2; WOW64)
    AppleWebKit/535.24 (KHTML, like Gecko)
    Chrome/19.0.1055.1 Safari/535.24"""
