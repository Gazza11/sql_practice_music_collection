from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def create_artist(artist):
    sql = "INSERT INTO albums (artist_name) VALUES (%s) RETURNING *"
    values = [artist.artist_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist