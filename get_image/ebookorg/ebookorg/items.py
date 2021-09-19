# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import TakeFirst, MapCompose, Join

class EbookorgItem(scrapy.Item):
    img_url = scrapy.Field()
    title = scrapy.Field(
        output_processor = Join(' ')
    )
