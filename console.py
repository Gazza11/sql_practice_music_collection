import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist('Gary Oldman')
artist2 = Artist('Travis Oliphant')
artist_repository.create_artist(artist1)
artist_repository.create_artist(artist2)

album_1 = Album("Roll With It", artist1, "Rock")
album_repository.save(album_1)
album_2 = Album("Another Album", artist1, "Pop")
album_repository.save(album_2)

album_1.genre = 'Pop'
album_repository.update(album_1)

artist_repository.select_all():
    print(album.__dict__)


pdb.set_trace()