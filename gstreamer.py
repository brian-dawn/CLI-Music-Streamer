# This is the gstreamer backend.
# The music backends should run in the background.

# TODO:
# Trigger for music ending, I think this is just a callback.
# Seek functions.

from gi.repository import GObject, Gst


GObject.threads_init()
Gst.init(None)

player = Gst.ElementFactory.make('playbin', 'player')

# Start playing music, if we are already playing a song stop the old one, start the new one.
def stream_uri(uri):

    player.set_state(Gst.State.READY)
    player.set_property('uri', uri)
    player.set_state(Gst.State.PLAYING)


# I believe this is a float between 0.0 and 10.0.
def set_volume(volume):

    player.set_property('volume', volume)


# Pause the stream.
def pause():

    player.set_state(Gst.State.PAUSED)


# Resume a paused song.
def resume():

    player.set_state(Gst.State.PLAYING)
