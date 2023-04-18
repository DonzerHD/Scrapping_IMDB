# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
ATLAS_KEY = os.getenv("ATLAS_KEY")

class ScrappingImdbPipeline:
    def process_item(self, item, spider):
        return item

class MongoDBMoviePipeline:
    def open_spider(self, spider):
        self.client = MongoClient(ATLAS_KEY)
        self.db = self.client["movies_db"]
        self.collection = self.db["movies_collection"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if spider.name == 'top_movies':
            self.movies_collection.insert_one(dict(item))
        elif spider.name == 'top_series':
            self.series_collection.insert_one(dict(item))
        return item