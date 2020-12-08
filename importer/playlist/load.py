def load_playlists(playlists):
    return [load_playlist(playlist) for playlist in playlists]


def load_playlist(playlist):
    with open(playlist, encoding='utf-8') as list:
        return list.read().splitlines()