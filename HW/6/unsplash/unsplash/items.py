# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UnsplashItem(scrapy.Item):
    category = scrapy.Field()
    author = scrapy.Field()
    title= scrapy.Field()
    published_on = scrapy.Field()
    camera = scrapy.Field()
    image_urls = scrapy.Field()
    tags = scrapy.Field()
    images = scrapy.Field()