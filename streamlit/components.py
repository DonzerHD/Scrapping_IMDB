import streamlit as st
import pandas as pd
import random


def display_movies(movies):
    for movie in movies:
        col1, col2, col3 = st.columns([2, 4, 4])
        with col1:
            image = movie['link_image']
            st.image(image, use_column_width=True)
        with col2:
            st.write(f"**Titre : {movie['title']}**")
            st.write(f"*Genre :{movie['genre']}*")
            st.write(f"Year : {movie['year']} - {movie['time']} min - Note : {movie['score']}")
            st.write(f"Acteurs : {movie['actor']}")
        with col3:
            st.write(f"_Synopsis_ : {movie['description']}")
            video_url = movie['link_video']
            if video_url:
               st.video(video_url)
            else:
                st.write("Aucune bande-annonce disponible")
        st.write("")

def search_movies(collection, name, genres, note, acteurs, time , limit=30):
    query = {}
    
    # Recherche par titre
    if name:
        query["title"] = {"$regex": f".*{name}.*", "$options": "i"}
    
    # Recherche par genre
    if genres:
        query["genre"] = {"$in": genres}

    # Recherche par note
    if note:
        query["score"] = {"$in": note}

    if acteurs:
        actors_query = []
        for actor in acteurs:
            actors_query.append({"actor": {"$regex": f".*{actor}.*", "$options": "i"}})
        query["$and"] = actors_query
            
    if time:
        query["time"] = {"$lte": int(time)}

    # Recherche dans la collection
    movies = collection.find(query).limit(limit)
    count = collection.count_documents(query)

    if count > 0:
        display_movies(movies)
    else:
        st.write("Aucun film trouvé")