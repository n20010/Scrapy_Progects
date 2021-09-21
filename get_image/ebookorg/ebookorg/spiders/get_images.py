import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from time import sleep
import re
import logging

from ebookorg.items import EbookorgItem
from scrapy.loader import ItemLoader


class GetImagesSpider(CrawlSpider):
    input_raw = input("add url: ")
    input_start_urls = input_raw.replace('https://', '')
    input_domains = re.sub('org.+$', 'org', input_start_urls)

    name = 'get_images'
    allowed_domains = [input_domains]
    start_urls = [input_raw]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="gdtm"]/div/a')), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths=('//table[@class="ptb"]/tbody/tr/td[last()]/a')), follow=True)
    )

    def parse_item(self, response):
        #logging.info(response.url)

        sleep(5)
        loader = ItemLoader(item=EbookorgItem(), response = response)
        loader.add_xpath('title', '//h1/text()')
        loader.add_value('img_url', response.xpath('//img[@id="img"]/@src').get())
        yield loader.load_item()

        #yield {
        #    "img_url": response.xpath('//img[@id="img"]/@src').get(),
        #}