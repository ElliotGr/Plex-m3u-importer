def load_playlists(playlists):
    return [load_playlist(playlist) for playlist in playlists]


def load_playlist(playlist):
    with open(playlist, encoding='ANSI') as list:
        return list.read().splitlines()