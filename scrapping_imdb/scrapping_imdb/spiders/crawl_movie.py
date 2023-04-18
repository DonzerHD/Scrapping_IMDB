from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MovieItem
import logging
from termcolor import colored

class IMDbTop250Movie(CrawlSpider):
    name = 'top_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']
    movie_count = 0

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }

    rules = (
        Rule(LinkExtractor(restrict_css=".titleColumn a"), callback="parse_movie"),
    )

    def parse_movie(self, response):
        title = response.css("h1[data-testid='hero__pageTitle'] span::text").get().strip()
        genre = response.css('a.ipc-chip--on-baseAlt span.ipc-chip__text::text').getall()

        # Incrémentation du compteur et affichage d'un message d'information coloré
        self.movie_count += 1
        log_message = colored(f"Film {self.movie_count}: {title}", 'cyan')
        logging.info(log_message)

        movie_item = MovieItem()
        movie_item['title'] = title
        movie_item['genre'] = genre

        yield movie_item