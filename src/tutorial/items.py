# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CollegesItem(scrapy.Item):
    title = scrapy.Field()
    imageUrl = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()