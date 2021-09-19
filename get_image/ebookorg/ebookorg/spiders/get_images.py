import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from time import sleep
import logging

from ebookorg.items import EbookorgItem
from scrapy.loader import ItemLoader


class GetImagesSpider(CrawlSpider):
    name = 'get_images'
    allowed_domains = ['e-hentai.org']
    start_urls = ['https://e-hentai.org/g/1813545/ce50f39ae8/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="gdtm"]/div/a')), callback='parse_item', follow=False),
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