import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()
album_repository.delete_all()

artist_1 = Artist("Eminem")
artist_repository.save(artist_1)
artist_2 = Artist("Depeche Mode")
artist_repository.save(artist_2)
artist_3 = Artist("Bo Burnham")
artist_repository.save(artist_3)
all_artists = artist_repository.select_all()
# pdb.set_trace()
# artist_repository.delete_all()
result = artist_repository.find_by_id(5)

album_1 = Album("Inside", "comedy", artist_3)
album_repository.save(album_1)

album_2 = Album("Curtain Call", "Rap", artist_1)
album_result = album_repository.save(album_2)

# result = album_repository.select_all()
# result = album_repository.find_by_id(41)
result = artist_repository.find_album(artist_3)

pdb.set_trace()
