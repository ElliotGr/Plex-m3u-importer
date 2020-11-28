import pygtrie

def index_library(library):
    all_songs = pygtrie.StringTrie()
    for album in library.albums():
        for track in album.tracks():
            all_songs[track.media[0].parts[0].file] = track

    ##for (key, value) in all_songs.items():
        ##print(key)
        ##print(value.title)
    return all_songs