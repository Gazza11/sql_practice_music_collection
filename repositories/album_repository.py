from pdb import run
from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album
import artist_repository as artist_repository


# Create the album
def create_album(album):
    sql = "INSERT INTO albums (album_name, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.album_name, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


def select():
    album = None

    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['album_name'], artist, result['genre'], result['id'])
    return album


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['album_name'], artist, row['genre'])
    return album


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(album):
    sql = "UPDATE albums SET (album_name, artist_id, genre) = (%s, %s, %s) WHERE id = %s"
    values = [album.album_name, album.artist.id, album.genre]
    run_sql(sql, values)