from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album


# Create the album
def create_album(album):
    sql = "INSERT INTO albums (album_name, artist, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.album_name, album.artist, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album