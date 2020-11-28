from importer.connection.connect import get_library, get_server
from importer.connection.setup import load_config
from importer.indexing.index import index_library
from importer.playlist.load import load_playlist
from importer.playlist.upload import upload_playlist

if __name__ == '__main__':
    config = load_config()
    server = get_server(config['server'], config['user'], config['pass'])
    library = get_library(server, config['library'])
    indexed_library = index_library(library)
    playlist_file = load_playlist()
    upload_playlist(playlist_file, indexed_library, server)