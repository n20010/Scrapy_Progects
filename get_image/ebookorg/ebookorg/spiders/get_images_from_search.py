import scrapy
from time import sleep
import re
import pprint
import logging
from ebookorg.items import EbookorgItem
from scrapy.loader import ItemLoader

class GetImagesFromSearchSpider(scrapy.Spider):
    input_raw = input("add url: ")
    input_start_urls = input_raw.replace('https://', '')
    input_domains = re.sub('org.+$', 'org', input_start_urls)

    name = 'get_images_from_search'
    allowed_domains = [input_domains]
    start_urls = [input_raw]

    def parse(self, response):
        index_list = response.xpath('//div[@class="glink"]/../@href').getall()
        global titles
        titles = {}
        for images_page in index_list:
            yield response.follow(url=images_page, callback=self.parse_images)

        next = response.xpath('(//td[@class="ptds"]/following-sibling::td)[1]/a/@href').get()
        if next:
            self.wait_time
            yield response.follow(url=next, callback=self.parse)

    def parse_images(self, response):
        language = response.xpath('(//td[@class="gdt2"])[4]/text()').get()
        self.wait_time
        if re.match(r'Japanese.*$', language):
            pp = pprint.PrettyPrinter(indent=4)
            title_key = self.normalize_title(response.xpath('//h1[@id="gn"]/text()').get())
            title_main = self.normalize_title(response.xpath('//h1[@id="gj"]/text()').get())
            titles[title_key] = title_main
            pp.pprint(titles)
            images = response.xpath('//div[@class="gdtm"]/div/a/@href').getall()

            print(f'[*] {title_main} is Japanese Page')
            print(f'[*] URL: {response.url}')
            for image in images:
                yield response.follow(url=image, callback=self.get_image)
            next_images = response.xpath('(//td[@class="ptds"]/following-sibling::td)[1]/a/@href').get()
            if next_images:
                self.wait_time
                yield response.follow(url=next_images, callback=self.parse_images)
    
    def get_image(self, response):
        self.wait_time
        title_key = self.normalize_title(response.xpath('//div[@id="i1"]/h1/text()').get())
        loader = ItemLoader(item=EbookorgItem(), response = response)
        loader.add_value('title', titles[title_key])
        loader.add_value('img_url',  response.xpath('//img[@id="img"]/@src').get())
        yield loader.load_item()
        

    def wait_time(self):
        sleep(4)
    
    def normalize_title(self, title):
        print(title)
        return title