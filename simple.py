#!/usr/bin/python2

# This is a really simple frontend to verify that the modules all work correctly.

import getpass

import googlemusic as gm
import gstreamer as gs


uname = raw_input('username: ')
passw = getpass.getpass('password: ')

devices = gm.get_registered_devices(uname, passw)
devices = filter(lambda s: s['type'] == 'PHONE', devices)

choices = []

for device, index in zip(devices, range(len(devices))):

    print index, device['model'], device['id']
    choices.append(device['id'])

device_id = choices[int(raw_input('select which device ID to use: '))][2:] # Omit 0x.

gm.set_registered_device(device_id)
gm.init(uname, passw)

while True:

    song_name = raw_input('select song name: ')

    results = gm.find_song(song_name)
    choices = []

    for result, index in zip(results, range(len(results))):

        print index, '\t\t\t'.join([result['song'], result['artist'], result['album']]).encode('ascii', 'ignore')
        choices.append(result['id'])

    uri = gm.get_uri(choices[int(raw_input('select which song to play: '))])

    gs.stream_uri(uri)
    gs.set_volume(3)
