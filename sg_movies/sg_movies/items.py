# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SgMoviesItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    duration = scrapy.Field()
    genre = scrapy.Field()
    lang = scrapy.Field()
    opening = scrapy.Field()
    rating = scrapy.Field()
    synopsis = scrapy.Field()
    poster = scrapy.Field()
