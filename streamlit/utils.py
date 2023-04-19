import pymongo
import os
from dotenv import load_dotenv
import requests
import re

load_dotenv()
ATLAS_KEY = os.getenv("ATLAS_KEY")

def get_db_connection():
    client = pymongo.MongoClient(ATLAS_KEY)
    db = client["imdb_top"]
    collection = db["top_movies"]
    return collection

def get_unique_genres(collection):
    unique_genres = collection.distinct("genre")
    return unique_genres

def get_unique_scores(collection):
    unique_scores = collection.distinct("score")
    return unique_scores

def get_unique_actors(collection):
    unique_actors = collection.distinct("actor")
    return unique_actors