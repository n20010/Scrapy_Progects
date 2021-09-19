import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from kinokuniya.items import BookItem
from scrapy.loader import ItemLoader

class ComputerBooksSpider(CrawlSpider):
    name = 'computer_books'
    allowed_domains = ['www.kinokuniya.co.jp']
    start_urls = ['https://www.kinokuniya.co.jp/disp/CSfDispListPage_001.jsp?dispNo=101005012&author=%E4%B8%8A%E7%94%B0%E6%83%87%E7%94%9F']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3[@class="heightLine-2"]/a'), callback='parse_item', follow=False),
      #  Rule(LinkExtractor(restrict_xpaths='(//a[contains(text(), "次へ")])[1]')),
    )

    def get_title(self, title):
        if title:
            return ' '.join(title).lstrip()
        return title

    def get_price(self, price):
        if price:
            return int(price.replace("¥", "").replace(',', ''))
        return 0

    def get_isbn(self, isbn):
        if isbn:
            return int(isbn.replace('ISBN：', ''))
        return isbn

    def parse_item(self, response):

        loader = ItemLoader(item=BookItem(), response = response)
        loader.add_xpath('title', '//h3[@itemprop="name"]/text()')
        loader.add_xpath('author', '//div[@class="infobox ml10 mt10"]/ul/li[1]/a/text()')
        loader.add_xpath('price', '//span[@class="sale_price"]/text()')
        loader.add_xpath('publisher', '//a[contains(@href, "publisher-key")]/text()')
        loader.add_xpath('isbn', '//li[@itemprop="identifier"]/text()')

        yield loader.load_item()
        #yield {
        #    "title" : self.get_title(response.xpath('//h3[@itemprop="name"]/text()').getall()),
        #    'author': response.xpath('//div[@class="infobox ml10 mt10"]/ul/li[1]/a/text()').get(),
        #    'price' : self.get_price(response.xpath('//span[@class="sale_price"]/text()').get()),
        #    'publisher' : response.xpath('//a[contains(@href, "publisher-key")]/text()').get(),
        #    'isbn' : self.get_isbn(response.xpath('//li[@itemprop="identifier"]/text()').get())
        #}
