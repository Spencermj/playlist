import echonest.remix.audio as audio
import pyechonest.playlist as playlist
import sys
import os

def main(radio_type, paramaterList):
    collect = []
    if radio_type == "artist-radio":
        p = playlist.static(type=radio_type, artist=paramaterList)
    elif radio_type == "song-radio":
        p = playlist.static(type=radio_type, song=paramaterList)
    elif radio_type == "genre-radio":
        p = playlist.static(type=radio_type, genre=paramaterList)
    p = playlist.static(type="artist", artist=paramaterList)
    for song in p:
        print song.title

if __name__ == '__main__':
    try:
        radioType = sys.argv[1]
        criteriaList = []
        for i in range(len(sys.argv) - 2):
             criteriaList.append(sys.argv[i + 2])
    except:
        sys.exit(-1)
    main(radioType, criteriaList)
