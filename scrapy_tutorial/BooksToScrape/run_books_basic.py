import scrapy 
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(settings=get_project_settings())
process.crawl('books_fantasy')
process.start()
