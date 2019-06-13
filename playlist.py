import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import operator

# export SPOTIPY_CLIENT_ID='4c55ad4b6d5e449bbfd40c243fcfc899'
# export SPOTIPY_CLIENT_SECRET='71de183f0c0e4b528ebc1b8fb34eb286'
# export SPOTIPY_REDIRECT_URI='http://google.com'
# python3 playlist.py 9k4m1kk7mwvi1kp2oypyitrkr?si=Lib9bphmTWeUZBuPOXxd6w


def show_tracks(tracks,tt):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        #print ("   %d %32.32s %s" % (i, track['artists'][0]['name'],track['id'],track['name']))
        if track['name'] in TRACK:
            tt[track['name']] = tt[track['name']] + 1
        else:
            tt[track['name']] = 1
    return tt




def getTrackCounts(uu,tt):
    playlists = spotifyObject.user_playlist(uu, playlist_id='', fields=None)
    playlists_ids = []
    #print(playlists)
    for pp in playlists['items']:
        playlists_ids.append(pp['id'])
    for id in playlists_ids:
        playlist = spotifyObject.user_playlist(uu, playlist_id=id, fields='tracks,next')
        tracks = playlist['tracks']
        xx = show_tracks(tracks,tt)
    return xx
    #sorted_x = sorted(TRACK.items(), key=lambda kv: kv[1])
    #print(sorted_x[-1],sorted_x[-2],sorted_x[-3])

TRACK = {}
#username_list = ['yunus nalcı','alperen kayalar','onur şereflioğlu','erdal akçiçek','mert öktem','ömer gören'
#,'tolga öztürk','dilek çelik','mert yılmaz','deniz pullukçu','gülfem tümtürk','erdem bulut']
username_list = ['11123952975','11126416080','11127124163','11129392918','11135943668','11161732572'
,'11182416467','21mqnpcrh6sl7cemhg5t6a5ni','21omdjfghjnocttwpdjktxyui','21uelppumdms33kwpwh255ioy','edismspejnbycsvh089dqrw2q','unalomemid']
for u in username_list:
    username = sys.argv[1]
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'
    try:
	    token = util.prompt_for_user_token(username, scope) # add scope
    except (AttributeError, JSONDecodeError):
	    os.remove(f".cache-{username}")
	    token = util.prompt_for_user_token(username, scope) # add scope

    spotifyObject = spotipy.Spotify(auth=token)



    print(u)
    TRACK = getTrackCounts(u,TRACK)

sorted_x = sorted(TRACK.items(), key=lambda kv: kv[1])
print(sorted_x[-1],sorted_x[-2],sorted_x[-3])


