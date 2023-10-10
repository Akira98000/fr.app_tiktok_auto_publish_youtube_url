# Programme de Téléchargement et Découpage de Vidéos YouTube

Ce programme permet de télécharger des vidéos depuis YouTube, de les découper en segments de 1 minute 30 secondes, et de les publier automatiquement sur TikTok à des heures programmées.

## Pré-requis

- Python 3.x
- Modules Python : `pytube`, `moviepy`, `Flask`
- (Optionnel) Compte développeur TikTok et clés d'API pour la publication automatique sur TikTok

## Installation

1. Clonez le dépôt:
git clone 'https://github.com/Akira98000/fr.app_tiktok_auto_publish_youtube_url/'

2. Naviguez vers le dossier du projet:
cd fr.app_tiktok_auto_publish_youtube_url

3. Installez les dépendances:
pip install Flask pytube moviepy


## Utilisation

1. Lancez le serveur Flask:

2. Ouvrez un navigateur et allez à `http://127.0.0.1:5000/`.

3. Entrez l'URL de la vidéo YouTube que vous souhaitez télécharger et cliquez sur "Télécharger".

4. Une fois le téléchargement terminé, vous pouvez cliquer sur "Découper la dernière vidéo" pour diviser la vidéo en segments de 1 minute 30 secondes.

5. (Optionnel) Si vous avez configuré l'API TikTok, le programme peut également publier les segments vidéo sur TikTok à des heures programmées.

## Notes

- Assurez-vous d'avoir les droits nécessaires pour télécharger et republier des vidéos. Respectez les droits d'auteur.
- L'API TikTok pourrait avoir des restrictions. Consultez leur documentation officielle pour plus d'informations.

## Contribution

Les contributions sont les bienvenues! Ouvrez une Pull Request ou créez une Issue pour toute suggestion ou bug.

## Licence

Ce projet est sous licence MIT.
