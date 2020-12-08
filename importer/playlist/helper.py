def format_playlist_name(raw_list_name):
    # TODO: Make this less hacky - strip any leading folders?
    if raw_list_name.startswith('.\\'):
        return raw_list_name[2:-4]
    else:
        return raw_list_name[:-4]