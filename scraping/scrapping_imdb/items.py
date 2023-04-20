# items.py
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    """
    Définit la structure de l'élément d'un film à extraire.

    Les champs de l'élément comprennent le titre, le score, le genre, l'année, la durée,
    la description, les acteurs, le public, le pays, la langue, le titre original,
    le lien vers l'image du film, l'URL de la page du trailer et le lien vers la vidéo du trailer.

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
        link_image (scrapy.Field): Lien vers l'image du film.
        trailer_page_url (scrapy.Field): URL de la page du trailer.
        trailer_video (scrapy.Field): Lien vers la vidéo du trailer.
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
    link_image = scrapy.Field()
    trailer_page_url = scrapy.Field()
    trailer_video = scrapy.Field()


class SerieItem(scrapy.Item):
    """
    Définit la structure de l'élément d'une série à extraire.

    Les champs de l'élément comprennent le titre, le score, le genre, l'année, la description,
    les acteurs et le public.

    Attributes:
        title (scrapy.Field): Titre de la série.
        score (scrapy.Field): Score de la série.
        genre (scrapy.Field): Genre(s) de la série.
        year (scrapy.Field): Année de sortie de la série.
        description (scrapy.Field): Description de la série.
        actor (scrapy.Field): Acteurs de la série.
        public (scrapy.Field): Classification de la série.
    """

    title = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    year = scrapy.Field()
    description = scrapy.Field()
    actor = scrapy.Field()
    public = scrapy.Field()
