def load_playlist():
    with open('playlist.m3u', encoding='utf-8') as list:
        return list.read().splitlines()