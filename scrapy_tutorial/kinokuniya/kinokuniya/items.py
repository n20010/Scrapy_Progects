# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join

def strip_yen(element):
    if element:
        return element.replace('¥', '')
    return element

def strip_tokka(element):
    if element:
        return element.replace('特価 ', '')
    return element


def strip_comma(element):
    if element:
        return element.replace(',', '')
    return element


def convert_int(element):
    if element:
        return int(element)
    return 0


def  strip_isbn(element):
    if element:
        return element.replace('ISBN：', '')
    return element


class BookItem(scrapy.Item):
    # define the fields for your item here like:

    title = scrapy.Field(
        input_processor = MapCompose(str.lstrip),
        output_processor = Join(' ')
    )
    author= scrapy.Field(
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor = MapCompose(strip_tokka, strip_yen, strip_comma, convert_int),
        output_processor = TakeFirst()
    )
    publisher = scrapy.Field(
        output_processor = TakeFirst()
    )
    isbn = scrapy.Field(
        input_processor = MapCompose(strip_isbn, convert_int),
        output_processor = TakeFirst()
    )

    image_urls = scrapy.Field(
    )