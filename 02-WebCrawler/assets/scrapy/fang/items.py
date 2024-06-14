# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CommunityItem(scrapy.Item):
    ''' 小区
    '''
    name = scrapy.Field()
    link = scrapy.Field()
    category = scrapy.Field()
    district = scrapy.Field()
    region = scrapy.Field()
    address = scrapy.Field()
    price_psm = scrapy.Field()
    parking = scrapy.Field()
