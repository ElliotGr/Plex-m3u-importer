# Plex-m3u-importer
This is a simple script to import .m3u playlists to a remote plex server. This is similar to https://github.com/dakusan/PlexPlaylistImporter but does not have the limitation of needing to be run on the same machine as the server.
## Installation
Can install in a new venv using
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Alternatively the releases will include a standalone windows binary to use.
## How to use?
First, a config.json file must be written (see config.json.example for formatting). Then, can be run from command line using
```bash
python m3u_importer playlist_1.m3u playlist_2.m3u
```