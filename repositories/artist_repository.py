from re import L
from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

# Create Artist
def create_artist(artist):
    sql = "INSERT INTO artists (artist_name) VALUES (%s) RETURNING *"
    values = [artist.artist_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


# SELECT ALL ARTISTS
def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['artist_name'], row['id'])
        artists.append(artist)
    return artists

# SELECT ARTIST
def select(id):
    artist = None

    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['artist_name'], result['id'])
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM astists WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(artist):
    sql = "UPDATE artists SET (artist_name) = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)

def albums(artist):
    albums = []

    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['album_name'], artist, row['genre'], row['id'])
        albums.append(album)
    return albums