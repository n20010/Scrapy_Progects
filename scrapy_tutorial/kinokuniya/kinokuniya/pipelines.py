# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import logging

from scrapy.pipelines.images import ImagesPipeline

class customImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        name = str(item.get('isbn')) + '.jpg'
        filename = r'computer_books\\' + name
        return  filename
        #return request.url.split('/')[-1]

class CheckItemPipeLine:
    def process_item(self, item, spider):
        if not item.get('isbn'):
           raise DropItem("Missing ISBN") 
        return item
