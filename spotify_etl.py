import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import json
from datetime import datetime


def run_spotify_new_releases_etl():
    # Set your Spotify API credentials
    client_id = "your Spotify ID"
    client_secret = "your Spotify secret key"

    # Authentication - Without user
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # Fetch new releases (you can specify a country code if desired)
    new_releases = sp.new_releases(limit=50, country='US')  # You can increase the limit up to 50 and specify the country code
    
    # Prepare list to hold release data
    new_releases_list = []
    
    for album in new_releases['albums']['items']:
        release_info = {
            'album_name': album['name'],
            'artist_name': album['artists'][0]['name'],
            'release_date': album['release_date'],
            'total_tracks': album['total_tracks'],
            'album_url': album['external_urls']['spotify']
        }
        new_releases_list.append(release_info)

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(new_releases_list)
    # df.to_csv("spotify_new_releases.csv", index=False)
    df.to_csv("s3://spotify-etl-project9613/spotify_new_releases.csv")
    

# Run the ETL function
# run_spotify_new_releases_etl()


