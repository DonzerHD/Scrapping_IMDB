# pipelines.py
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
ATLAS_KEY = os.getenv("ATLAS_KEY")


class ScrappingImdbPipeline:
    def process_item(self, item, spider):
        return item


class MongoDB_IMDB_TopPipeline:
    """
    Pipeline pour stocker les données dans une base de données MongoDB.

    Les éléments sont stockés dans différentes collections en fonction de leur type (films, séries ou documentaires).

    Attributes:
        client (MongoClient): Client MongoDB.
        db (Database): Base de données MongoDB.
        movies_collection (Collection): Collection pour les films.
        series_collection (Collection): Collection pour les séries.
    """

    def open_spider(self, spider):
        """
        Initialise la connexion à la base de données MongoDB et les collections
        lors de l'ouverture du spider.

        Args:
            spider (scrapy.Spider): Le spider qui est en cours d'exécution.
        """
        self.client = MongoClient(ATLAS_KEY)
        self.db = self.client["imdb_top"]
        self.movies_collection = self.db["top_movies"]
        self.series_collection = self.db["top_series"]

    def close_spider(self, spider):
        """
        Ferme la connexion à la base de données MongoDB lors de la fermeture du spider.

        Args:
            spider (scrapy.Spider): Le spider qui est en cours de fermeture.
        """
        self.client.close()

    def process_item(self, item, spider):
        """
        Traite et insère l'élément dans la collection appropriée en fonction du nom du spider.

        Args:
            item (scrapy.Item): L'élément à insérer dans la base de données.
            spider (scrapy.Spider): Le spider qui est en cours d'exécution.

        Returns:
            item (scrapy.Item): L'élément après avoir été traité et inséré.
        """
        if spider.name == 'top_movies':
            self.movies_collection.insert_one(dict(item))
        elif spider.name == 'top_series':
            self.series_collection.insert_one(dict(item))
        return item
