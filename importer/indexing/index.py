import pygtrie

def index_library(library):
    all_songs = pygtrie.Trie()
    for album in library.albums():
        for track in album.tracks():
            all_songs[track.media[0].parts[0].file] = track
    return all_songs