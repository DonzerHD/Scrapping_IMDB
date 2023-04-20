import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
ATLAS_KEY = os.getenv("ATLAS_KEY")

def get_db_connection():
    """Établit une connexion à la base de données MongoDB Atlas et retourne la collection."""
    client = pymongo.MongoClient(ATLAS_KEY)
    db = client["imdb_top"]
    collection = db["top_movies"]
    return collection

def get_unique_genres(collection):
    """Récupère et retourne les genres uniques de la collection."""
    unique_genres = collection.distinct("genre")
    return unique_genres

def get_unique_scores(collection):
    """Récupère et retourne les scores uniques de la collection."""
    unique_scores = collection.distinct("score")
    return unique_scores

def get_unique_actors(collection):
    """Récupère et retourne les acteurs uniques de la collection."""
    unique_actors = collection.distinct("actor")
    return unique_actors