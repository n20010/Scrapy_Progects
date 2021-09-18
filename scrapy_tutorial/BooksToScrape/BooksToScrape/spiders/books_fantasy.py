import scrapy


class BooksFantasySpider(scrapy.Spider):
    name = 'books_fantasy'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html']

    def parse(self, response):
        pods = response.xpath("//h3/a")
        for pod in pods:
            title = pod.xpath(".//text()").get()
            url = pod.xpath(".//@href").get()
            yield {
                "title" : title,
                "url" : url
            }

        next = response.xpath('//li[@class="next"]/a/@href')
        if next:
            yield response.follow(url = next[0], callback=self.parse)

