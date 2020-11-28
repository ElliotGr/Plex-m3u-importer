def index_library(library):
    all_songs = []
    for album in library.albums():
        for track in album.tracks():
            for media in track.media:
                for part in media.parts:
                    all_songs.append(part.file)
                    print(part.file)
    return all_songs