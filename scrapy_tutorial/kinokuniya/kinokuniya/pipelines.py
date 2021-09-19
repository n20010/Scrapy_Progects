# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class CheckItemPipeLine:
    def process_item(self, item, spider):
        if not item.get('isbn'):
           raise DropItem("Missing ISBN") 
        return item
