import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SerieItem


class CrawlSeriesSpider(CrawlSpider):
    name = "crawl_series"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"]
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250', headers={
            'User-Agent': self.user_agent
        })


    rules = (Rule(LinkExtractor(restrict_css=".titleColumn > a"), callback="parse_series"),)

    def parse_series(self, response):
        title = response.css("h1[data-testid='hero__pageTitle'] span::text").get().strip()
        score = response.css("span.sc-bde20123-1.iZlgcd::text").get()
        # genre = response.css("div.ipc-chip-list__scroller a.ipc-chip.ipc-chip--on-baseAlt::text").getall()
        year = response.css("ul.ipc-inline-list.ipc-inline-list--show-dividers.sc-afe43def-4.kdXikI.baseAlt a.ipc-link.ipc-link--baseAlt.ipc-link--inherit-color::text").get()
        # time = response.css("ul.ipc-inline-list.ipc-inline-list--show-dividers.sc-afe43def-4.kdXikI.baseAlt::text").get()[-1]  # le [-1] pour prendre le dernier li
        description = response.css("span.sc-5f699a2-2.cxqNYC::text").get()
        # actor = response.css(".ipc-metadata-list-item__list-content-item--link::text").getall()       
        public = response.css("ul.ipc-inline-list.ipc-inline-list--show-dividers.sc-afe43def-4.kdXikI.baseAlt li:nth-child(3) a::text").get()
        # country = response.css("a.ipc-metadata-list-item__list-content-item.ipc-metadata-list-item__list-content-item--link::text").getall()

        
        serie_item = SerieItem()
        serie_item['title'] = title
        serie_item['score'] = score
        # serie_item['genre'] = genre
        serie_item['year'] = year
        # serie_item['time'] = time
        serie_item['description'] = description
        # serie_item['actor'] = actor
        serie_item['public'] = public
        # serie_item['country'] = country

        yield serie_item