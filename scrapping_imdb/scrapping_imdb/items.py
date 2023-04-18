# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    year = scrapy.Field()
    time = scrapy.Field()
    description = scrapy.Field()
    actor = scrapy.Field()
    public = scrapy.Field()
    country = scrapy.Field()
    language = scrapy.Field()
    original_title = scrapy.Field()
