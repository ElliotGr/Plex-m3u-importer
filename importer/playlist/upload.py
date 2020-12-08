from importer.playlist.helper import format_playlist_name
from importer.playlist.load import load_playlists


def upload_playlists(playlists, indexed_library, server):
    playlist_files = load_playlists(playlists)
    for file, name in zip(playlist_files, playlists):
        upload_playlist(file, name, indexed_library, server)


def upload_playlist(playlist, name, indexed_library, server):
    item_list = create_item_list(playlist, indexed_library)
    create_playlist(item_list, format_playlist_name(name), server)


def create_item_list(playlist, indexed_library):
    item_list = []
    for filename in playlist:
        if indexed_library.has_key(filename):
            item_list.append(indexed_library[filename])
        else:
            print('unable to find file ' + filename)
    return item_list


def create_playlist(item_list, name, server):
    server.createPlaylist(name, item_list)
