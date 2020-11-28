from plexapi.myplex import MyPlexAccount


def get_server(server, user, password):
    account = authenticate(user, password)
    return connect(server, account)


def get_library(server, library):
    return server.library.section(library)


def authenticate(user, password):
    return MyPlexAccount(user, password)


def connect(server, account):
    return account.resource(server).connect()