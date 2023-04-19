import streamlit as st
from components import search_movies
from utils import get_db_connection, get_unique_genres , get_unique_scores , get_unique_actors

def main():
    st.set_page_config(page_title="Mon application de films", page_icon=":movie_camera:")
    collection = get_db_connection()

    st.title("Recherche de films")

    # Organiser les éléments de recherche et les filtres dans des colonnes
    col1, col2 = st.columns([3, 1])

    # Recherche par titre
    name = col1.text_input("Rechercher par titre")

    # Recherche par genre
    genre_list = get_unique_genres(collection)
    selected_genres = col2.multiselect("Filtrer par genre", genre_list)

    # Recherche par note
    score_list = get_unique_scores(collection)
    selected_scores = col2.selectbox("Filtrer par note minimale", [""] + score_list)

    # Recherche par acteur
    actor_list = get_unique_actors(collection)
    selected_actors = col2.multiselect("Filtrer par acteur(s)", actor_list)

    # Recherche par durée
    time_movie = col2.text_input("Filtrer par durée (en minutes)")

    # Lancer la recherche avec les filtres
    search_movies(collection, name, selected_genres, selected_scores, selected_actors, time_movie)
    
if __name__ == "__main__":
    main()