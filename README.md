# Scrapping_IMDB
Ce projet est une application de recherche de films et de séries construite avec Streamlit et Python. Les données sont extraites du site IMDb à l'aide de Scrapy et stockées dans une base de données MongoDB. L'utilisateur peut rechercher des films ou séries en fonction de leur titre, genre, note, acteurs et durée, et trier les résultats par note.

### Remarque :
- **Pour l'instant, seuls les 250 meilleurs films et séries ont été récupérés par scraping et seuls les films correspondants sont disponibles dans l'application Streamlit.**
- **Les liens vers les bandes-annonces fournies peuvent ne pas fonctionner en raison des modifications régulières apportées par IMDb**

## Cette application est déployée avec Streamlit Community Cloud pour y accéder cliquez sur le badge ci-dessous :
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://donzerhd-scrapping-imdb-streamlitapp-60xthx.streamlit.app/)

## Structure du projet

Le projet est organisé en plusieurs dossiers :

- `data` : contient les fichiers csv .
- `notebook` : contient les notebooks Jupyter pour les questions .
- `scraping` : contient les scripts Scrapy pour extraire les données du site IMDb .
- `streamlit` : contient les fichiers Python et les composants Streamlit pour l'interface utilisateur de l'application .

## Installation

1. Clonez ce dépôt : `git clone git@github.com:DonzerHD/Scrapping_IMDB.git`
2. Créez un environnement virtuel pour ce projet pour installer les dépendances .
3. Installez les dépendances : `pip install -r requirements.txt`

## Scrapping 

Pour lancer le scrapping, il faut se placer dans le dossier `scraping` et lancer les commandes suivantes :
 - `scrapy crawl top_movies -o ../data/top_movies.csv` pour extraire les données des films
 - `scrapy crawl top_series -o ../data/top_series.csv` pour extraire les données des séries

Attention des fichiers csv sont déjà présents dans le dossier `data` supprimer les avant de lancer le scrapping.

## MongoDB

Créer bien un fichier `.env` dans le dossier `streamlit` et à la racine du projet pour y mettre les informations de connexion à la base de données MongoDB .
- Voila quoi mettre dans le fichier `.env` :
```ATLAS_KEY = "votre clé d'accès à la base de données MongoDB"```

## Pipeline
Décommenter la ligne 97 dans le fichier `scraping/scrapping_imdb/settings.py` pour lancer le pipeline et enregistrer les données dans la base de données MongoDB.

## Streamlit
Pour lancer l'application, il faut se placer dans le dossier `streamlit` et lancer la commande suivante : `streamlit run app.py`

## Docker
- Pour lancer l'application avec Docker, il faut se placer dans le dossier `streamlit` et lancer un build de l'image Docker avec la commande suivante : `docker build -t nom_de_l'image .`
- Vous pouvez changer le port dans le fichier `Dockerfile` si vous le souhaitez.
- Pour lancer l'application, il faut lancer un container avec la commande suivante : `docker run -p port:port nom_de_l'image`
- Ensuite récupérer l'ip dans la console et coller l'ip dans votre navigateur avec le port.
- Pour le push sur Docker Hub, il faut se connecter à votre compte Docker Hub.
- Puis lancer la commande suivante : `docker login` et rentrer votre nom d'utilisateur et mot de passe.
- Ensuite lancer la commande suivante : `docker tag nom_de_l'image nom_d'utilisateur/nom_de_l'image`
- Pour finir lancer la commande suivante : `docker push nom_d'utilisateur/nom_de_l'image`

## Utilisation de Microsoft Azure
Voici les étapes pour utiliser Microsoft Azure :
- Créez un compte Microsoft Azure ou connectez-vous à un compte existant.
- Accédez à la section "Container Instances" et cliquez sur "Create".
- Suivez les étapes pour créer un conteneur.
- Dans la section "Source d'image", sélectionnez "Other Registry" et entrez le nom de l'image Docker, par exemple : nom_utilisateur/nom_image.
- Dans la section "Port", sélectionnez "TCP" et entrez le port que vous avez mis dans le fichier Dockerfile.
- Ensuite, dans la section "Advanced", créez votre clé ATLAS_KEY. Dans la clé, entrez "ATLAS_KEY" et dans la valeur, entrez la clé d'accès à la base de données MongoDB que vous avez mise dans le fichier .env. Notez que Microsoft Azure ne prend pas en compte les variables d'environnement dans le fichier .env, vous devez donc entrer manuellement la clé.
- Enfin, cliquez sur "Review + create" et "Create" pour créer le conteneur.

### **Accéder à l'application déployée sur Microsoft Azure**
- Dans la section "Container Instances", cliquez sur le conteneur que vous venez de créer.
- Prendre l'IP_ADDRESS et le PORT et coller l'IP_ADDRESS dans votre navigateur avec le PORT que vous avez mis dans le fichier Dockerfile.

## License
Ce projet est sous licence MIT - voir [LICENSE](LICENSE) pour plus de détails.

## Auteurs
* **Thomas.l59**[@DonzerHD](https://github.com/DonzerHD)
* **Dylan.v59**[@vanstavelD](https://github.com/vanstavelD)



