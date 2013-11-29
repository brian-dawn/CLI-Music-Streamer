
# Since we can only have one backend of each type at a time I doubt we need classes.

# TODO:
# Currently this backend only searches through "All Access" I am unsure if this includes songs uploaded by the user.
# Search do we want to search for songs by an Arist? Or have a specific add artist option? Right now I only have it finding songs.

# Proper error handling.

from gmusicapi import Mobileclient
from gmusicapi import Webclient

session = None # A global should be fine, we only ever want one session per backend, at least at the moment.
device_id = None

# This method only needs to be run if we don't have any registered device IDs, which we need for the mobile API to work properly.
def get_registered_devices(login, password):

    websession = Webclient()
    websession.login(login, password)

    return websession.get_registered_devices()


# Assign to the global. This is needed for getting a valid mp3 URI later.
def set_registered_device(device):
    global device_id

    device_id = device


# Basic init for all possible backends. Different backends will presumably require different types of authentication information.
def init(login, password):
    global session

    session = Mobileclient()
    session.login(login, password)


# The dict returned will NOT return a valid URI, googlemusic URIs returned in a search are only valid for 1 minute.
# Therefore we simply store a unique ID that allows us to easily find the song when we want to play it.
def find_song(name):

    # TODO: We presumably should try/catch disconnects here.
    search = session.search_all_access(name)

    return [{'song':   hit['track']['title'],
             'artist': hit['track']['artist'],
             'album':  hit['track']['album'],
             'id':     hit['track']['nid']} for hit in search['song_hits']]


# Return a song URI. Once this is called the URI will only be valid for 1 minute.
def get_uri(song_id):

    return session.get_stream_url(song_id, device_id)

