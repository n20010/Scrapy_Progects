import scrapy


class BooksFantasySpider(scrapy.Spider):
    name = 'books_fantasy'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html']

    def parse(self, response):
        pods = response.xpath("//h3/a")
        for pod in pods:
        #    title = pod.xpath(".//text()").get()
        #    url = pod.xpath(".//@href").get()
        #    yield {
        #        "title" : title,
        #        "url" : url
        #    }
            yield response.follow(url = pod.xpath(".//@href").get(), callback=self.parse_item)

        next = response.xpath('//li[@class="next"]/a/@href').get()
        if next:
            yield response.follow(url = next[0], callback=self.parse)
    
    def parse_item(self, response):
        main_book_info = response.xpath('//div[@class="col-sm-6 product_main"]')
        yield {
            "title": main_book_info.xpath(".//h1/text()").get(),
            "price": main_book_info.xpath('.//p[@class="price_color"]/text()').get(),
            "stock": main_book_info.xpath('.//p[@class="instock availability"]/text()').get(),
            "rating": response.xpath('//p[3]/@class').get(),
            "UPC": response.xpath('//th[contains(text(), "UPC")]/following-sibling::td[1]/text()').get(),
            "review": response.xpath('//th[contains(text(), "Number of reviews")]/following-sibling::td[1]/text()').get()
        }

