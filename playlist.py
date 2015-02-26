import echonest.remix.audio as audio
import pyechonest.playlist as playlist
import sys
import os

def main():
    collect = []
    p = playlist.static(type='artist-radio', artist=['led zeppelin', 'rolling stones'])
    for song in p:
        print song.title

if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit(-1)

