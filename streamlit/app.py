import streamlit as st
from components import search_movies
from utils import get_db_connection, get_unique_genres, get_unique_scores, get_unique_actors


def main():
    """
    Application Streamlit pour rechercher des films en fonction de différents critères et filtres.
    """
    st.set_page_config(page_title="Movie App", page_icon=":movie_camera:", layout="wide")
    collection = get_db_connection()

    st.title("Movie Search")

    # Organiser les éléments de recherche et les filtres dans des colonnes
    col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 1])

    # Recherche par titre
    name = col1.text_input("Search by title")

    # Recherche par genre
    genre_list = get_unique_genres(collection)
    selected_genres = col2.multiselect("Filter by genre", genre_list)

    # Recherche par note
    score_list = get_unique_scores(collection)
    selected_scores = col3.selectbox("Filter by minimum rating", [""] + score_list)

    # Recherche par acteur
    actor_list = get_unique_actors(collection)
    selected_actors = col4.multiselect("Filter by actor(s)", actor_list)

    # Recherche par durée
    time_movie = col5.text_input("Filter by duration (in minutes)")

    # Filtre par ordre décroissant ou croissant de score
    sort_order = col6.radio("Sort by rating", ("Descending", "Ascending"))

    # Lancer la recherche avec les filtres
    search_movies(collection, name, selected_genres, selected_scores, selected_actors, time_movie, sort_order)


if __name__ == "__main__":
    main()