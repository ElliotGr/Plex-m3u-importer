def upload_playlist(playlist, indexed_library, server):
    list = create_item_list(playlist, indexed_library)
    create_playlist(list, server)


def create_item_list(playlist, indexed_library):
    list = []
    for filename in playlist:
        if indexed_library.has_key(filename):
            list.append(indexed_library[filename])
        else:
            print('unable to find file ' + filename)
    return list


def create_playlist(list, server):
    server.createPlaylist('imported_playlist', list)