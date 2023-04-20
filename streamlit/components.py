import streamlit as st
import pandas as pd

def display_movies(movies):
    """
    Affiche les informations des films dans l'application Streamlit.
    
    :param movies: Un itérable d'objets films (généralement des dictionnaires contenant des informations sur les films)
    """
    for movie in movies:
        col1, col2 = st.columns([1, 5])

        # Afficher l'image du film
        with col1:
            image = movie['link_image']
            st.image(image, use_column_width=True)

        # Afficher les informations sur le film
        with col2:
            st.write(f"# {movie['title']}")
            st.write(f"<font color='blue'>🎭 Genre</font> : {movie['genre']}  -   "
                     f"<font color='green'>📅 Year</font> : {movie['year']}  -   "
                     f"<font color='purple'>⏳ Duration</font> : {movie['time']} min  -   "
                     f"<font color='red'>⭐ Rating</font> : {movie['score']}",
                     unsafe_allow_html=True)
            st.write(f"🎬 Main Actors: {movie['actor']}")
            st.write(f"_Synopsis_: {movie['description']}")

            # Afficher la bande-annonce du film
            video_url = movie['trailer_video']
            if video_url:
                col_video = st.columns([1, 3, 1])  # Créez une nouvelle colonne avec des proportions ajustées
                with col_video[1]:  # Utilisez la colonne du milieu pour afficher la vidéo
                    st.video(video_url)
            else:
                st.write("No trailer available")

        st.write("")
        st.markdown("---")

def search_movies(collection, name, genres, note, acteurs, time, sort_order, limit=20):
    """
    Recherche des films en fonction des critères fournis.
    
    :param collection: La collection MongoDB où les données de films sont stockées
    :param name: Une chaîne de caractères pour rechercher un film par titre
    :param genres: Une liste de genres pour filtrer les films
    :param note: Une note minimale pour filtrer les films
    :param acteurs: Une liste d'acteurs pour filtrer les films qui les incluent
    :param time: Une durée maximale en minutes pour filtrer les films
    :param sort_order: Un ordre de tri ("Descending" ou "Ascending") pour trier les films en fonction de leur note
    :param limit: Un nombre entier pour limiter le nombre de résultats (par défaut à 20)
    """
    query = {}
    
    # Recherche par titre
    if name:
        query["title"] = {"$regex": f".*{name}.*", "$options": "i"}
    
    # Recherche par genre
    if genres:
        query["genre"] = {"$in": genres}

    # Recherche par note
    if note:
        query["score"] = {"$in": [note]}
        
    # Recherche par acteur
    if acteurs:
        actors_query = []
        for actor in acteurs:
            actors_query.append({"actor": {"$regex": f".*{actor}.*", "$options": "i"}})
        query["$and"] = actors_query
        
    # Recherche par durée  
    if time:
        query["time"] = {"$lte": int(time)}

    # Tri des résultats en fonction de l'ordre choisi
    if sort_order == "Descending":
        sort = [("score", -1)]
    else:
        sort = [("score", 1)]

    # Recherche dans la collection
    movies = collection.find(query).sort(sort).limit(limit)
    count = collection.count_documents(query)
    
    # Afficher les résultats
    if count > 0:
        display_movies(movies)
    else:
        st.write("No movies found")