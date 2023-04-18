# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    """
    Définit la structure de l'élément d'un film à extraire.

    Les champs de l'élément comprennent le titre, le score, le genre, l'année, la durée,
    la description, les acteurs, le public, le pays, la langue et le titre original.

    Attributes:
        title (scrapy.Field): Titre du film.
        score (scrapy.Field): Score du film.
        genre (scrapy.Field): Genre(s) du film.
        year (scrapy.Field): Année de sortie du film.
        time (scrapy.Field): Durée du film.
        description (scrapy.Field): Description du film.
        actor (scrapy.Field): Acteurs du film.
        public (scrapy.Field): Classification du film.
        country (scrapy.Field): Pays d'origine du film.
        language (scrapy.Field): Langue(s) du film.
        original_title (scrapy.Field): Titre original du film.
    """

    title = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    year = scrapy.Field()
    time = scrapy.Field()
    description = scrapy.Field()
    actor = scrapy.Field()
    public = scrapy.Field()
    country = scrapy.Field()
    language = scrapy.Field()
    original_title = scrapy.Field()
