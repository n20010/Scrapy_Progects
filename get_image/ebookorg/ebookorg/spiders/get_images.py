import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from time import sleep
import re
# import logging

from ebookorg.items import EbookorgItem
from scrapy.loader import ItemLoader


class GetImagesSpider(CrawlSpider):
    start_url = input("add url: ")
    input_domains = re.sub('org.+$', 'org', start_url.replace('https://', ''))

    name = 'get_images'
    allowed_domains = [input_domains]
    start_urls = [start_url]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="gdtm"]/div/a')), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths=('(//td[@class="ptds"]/following-sibling::td)[1]/a')), follow=True)
    )

    def parse_start_url(self, response):
        global title_main
        title_main = response.xpath('//h1[@id="gj"]/text()').get()

    def parse_item(self, response):
        sleep(3)
        loader = ItemLoader(item=EbookorgItem(), response = response)
        loader.add_value('title', title_main)
        loader.add_value('img_url', response.xpath('//img[@id="img"]/@src').get())
        yield loader.load_item()