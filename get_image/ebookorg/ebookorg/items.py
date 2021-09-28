# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import TakeFirst, MapCompose, Join

def strip_windows_fileFormat(element):
    if element:
        strip1 = element.replace('|', ' ')
        strip2 = strip1.replace('/', ' ')
        strip3 = strip2.replace('\\', ' ')
        strip4 = strip3.replace(':', ' ')
        strip5 = strip4.replace('*', ' ')
        strip6 = strip5.replace('?', ' ')
        strip7 = strip6.replace('<', ' ')
        strip8 = strip7.replace('>', ' ')
        strip9 = strip8.replace('"', ' ')
        return strip9
    return element

class EbookorgItem(scrapy.Item):
    img_url = scrapy.Field()
    title = scrapy.Field(
        input_processor = MapCompose(strip_windows_fileFormat),
        output_processor = Join(' ')
    )
