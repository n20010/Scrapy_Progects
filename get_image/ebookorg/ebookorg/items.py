# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import TakeFirst, MapCompose, Join

def strip_bar(element):
    if element:
        return element.replace('|', '')
    return element

def strip_slash(element):
    if element:
        return element.replace('/', '')
    return element


class EbookorgItem(scrapy.Item):
    img_url = scrapy.Field()
    title = scrapy.Field(
        input_processor = MapCompose(strip_bar, strip_slash),
        output_processor = Join(' ')
    )
