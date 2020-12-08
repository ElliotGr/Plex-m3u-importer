import argparse
import sys

from importer.connection.connect import get_library, get_server
from importer.connection.setup import load_config
from importer.indexing.index import index_library
from importer.playlist.upload import upload_playlists

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Import m3u files to a plex library')
    parser.add_argument('playlists', metavar='playlist.m3u', help='.m3u files to be imported', nargs='+')
    args = parser.parse_args()

    config = load_config()
    server = get_server(config['server'], config['user'], config['pass'])
    library = get_library(server, config['library'])
    indexed_library = index_library(library)
    upload_playlists(args.playlists, indexed_library, server)