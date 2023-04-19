import streamlit as st
import pandas as pd

def display_movies(movies):
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

    if acteurs:
        actors_query = []
        for actor in acteurs:
            actors_query.append({"actor": {"$regex": f".*{actor}.*", "$options": "i"}})
        query["$and"] = actors_query
            
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

    if count > 0:
        display_movies(movies)
    else:
        st.write("No movies found")