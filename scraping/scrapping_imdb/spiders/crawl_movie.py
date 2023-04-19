import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MovieItem
import scrapy
import logging
from termcolor import colored
from ..utils import time_to_minutes


class IMDbTop250Movie(CrawlSpider):
    """
    Spider pour récupérer les informations des 250 meilleurs films sur IMDb.
    """
    name = 'top_movies'
    allowed_domains = ['imdb.com']
    movie_count = 0
    film_counter = 0

    rules = (
        Rule(LinkExtractor(restrict_css=".titleColumn a"), callback="parse_movie"),
    )

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers={
            'User-Agent': self.user_agent
        })

    def parse_movie(self, response):
        title = response.css("h1[data-testid='hero__pageTitle'] span::text").get().strip()
        score = response.css("span.iZlgcd::text").get()
        genre = response.css('a.ipc-chip--on-baseAlt span.ipc-chip__text::text').getall()
        year = response.css('ul.sc-afe43def-4 li.ipc-inline-list__item a.ipc-link--inherit-color::text').get()
        time = response.css('ul.sc-afe43def-4 li.ipc-inline-list__item::text').get()
        time = time_to_minutes(time)
        description = response.css('span.sc-5f699a2-0::text').get()
        actor = list(set(response.css('li.ipc-metadata-list__item:contains("Stars") li.ipc-inline-list__item a.ipc-metadata-list-item__list-content-item--link::text').getall()))
        public = response.css('ul.sc-afe43def-4 li.ipc-inline-list__item a.ipc-link--inherit-color::text').getall()[-1]
        country = response.css('li.ipc-metadata-list__item[data-testid="title-details-origin"] a.ipc-metadata-list-item__list-content-item--link::text').getall()
        language = response.css('li.ipc-metadata-list__item[data-testid="title-details-languages"] a.ipc-metadata-list-item__list-content-item--link::text').getall()
        original_title = response.css('li.ipc-metadata-list__item:contains("Also known as") span.ipc-metadata-list-item__list-content-item::text').getall()
        link_image = response.css('div.ipc-media img.ipc-image::attr(src)').get()
        trailer_page_url = response.css('div.ipc-slate a.ipc-lockup-overlay::attr(href)').get()
            
        self.movie_count += 1
        log_message = colored(f"Film {self.movie_count}: {title}", 'cyan')
        logging.info(log_message)
        logging.info(f"url : {response.url}")

        movie_item = MovieItem()
        movie_item['title'] = title
        movie_item['score'] = score
        movie_item['genre'] = genre
        movie_item['year'] = year
        movie_item['time'] = time
        movie_item['description'] = description
        movie_item['actor'] = actor
        movie_item['public'] = public
        movie_item['country'] = country
        movie_item['language'] = language
        movie_item['original_title'] = original_title
        movie_item['link_image'] = link_image
        movie_item['trailer_page_url'] = "https://www.imdb.com" + trailer_page_url
        
        # Ajoutez 'yield' ici
        yield scrapy.Request(url=movie_item['trailer_page_url'], callback=self.parse_trailer, meta={'movie_item': movie_item})
        return
        
    def parse_trailer(self, response):
        movie_item = response.meta['movie_item']
        next_data_script = response.css('script[id="__NEXT_DATA__"]::text').get()
        next_data_json = json.loads(next_data_script)

        playback_urls = next_data_json['props']['pageProps']['videoPlaybackData']['video']['playbackURLs']
        
        video_480p_url = None
        for playback_url in playback_urls:
            if playback_url['displayName']['value'] == '480p':
                video_480p_url = playback_url['url'].replace('\\u0026', '&')
                break

        if video_480p_url:
            logging.info(f"Trailer video URL: {video_480p_url}")
            movie_item['trailer_video'] = video_480p_url
            yield movie_item
        else:
            logging.error("Couldn't find 480p video URL")

