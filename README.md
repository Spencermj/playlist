## playlist

Create a static playlist using Pyechonest

**What It Does**

Using [Playlist API], you can create an ordered list of tracks when given certain paramaters. [The Echonest Playlist Overview] goes in depth on what you can do with each of the methods in the API and how the playlist changes with each paramater. The Echonest also has guides on how to perform basic, standard, and premium playlisting. Using the playlist API, you can make a very basic playlist with a small amount of code or you can make a very advanced playlist.

**What Problem Does It Solve?**

The playlist module allows you to create a playlist based off either a Taste Profile or preferred music. This is obviously the resource you would want to use if you were making an application involving a playlist, but it can serve more than just that purpose. The playlist module finds songs that it considers similar to each other based off of a certain criteria, this is a very useful resource when you need to find songs that are related to each other in some way. To find similar songs all you need to do is make a playlist object using the songs you want and the criteria you want to use to find related songs.

**How Did I Come Up With This Idea?**

While thinking about what was required for a more complex program, I realized that I was in need of some way of creating a playlist. The idea of the original program was to make a playlist of songs that would sound well together and combine them into one .mp3. I originally thought that I would need to write my own code to pick which songs would go into the .mp3, but I quickly found that [The Echonest] has a playlist module as well as multiples guides on how to use it.

**Dependencies**

You will need Pyechonest to use playlist.py.

**Resources**

1. [Playlist API]

2. [The Echonest Playlisting Overview]

3. [The Echonest Standard Playlisting]

4. [Taste Profile]

**How To Create A Playlist**

There are many different paramaters that will affect the outcome of the playlist. To make a basic playlist, the only paramaters necessary are anywhere from one to five artists, genres, or songs and a playlist type. The following is a list of playlist types:

    artist-radio - Plays songs from the given artist(s) and similar artists.
    song-radio - Plays songs similar to the given song(s).
    genre-radio - Plays songs from artists relevant to the given genre.
    artist - Plays songs from only the given artist(s).
    catalog - Plays songs listed in the given Taste Profile.
    catalog-radio - Plays songs listed in the given Taste Profile, as well as similar artists and songs outside of the 
    Taste Profile.

With all the playlist types other than Catalog and Catalog-Radio, you can specify an attribute that will determine what songs are added to the playlist. Some of the allowed attributes include song hotttnesss, tempo, duration, loudness, mode, key, energy, and danceability. To provide more variety in a playlist, the limited_interactivity paramater can be set to true to cause the playlist to obey the following conditions:

    No more than 2 songs in a row from the same album
    No more than 3 songs from an album in a 3 hour period
    No more than 3 different songs in a row by the same artist
    No more than 4 songs by the same artist in a 3 hour period
    
The Catalog and Catalog-Radio playlist types are used when you are creating a playlist based off a [Taste Profile], a Taste Profile is a collection of artists and songs that gives much more information to the playlist than would be otherwise available. A Taste Profile can be kept and modified over time to keep track of an individual's personal tastes or it can be created to make a specific playlist based off of certain songs or artists.

**Example**

After importing the Playlist module, you can easily create a playlist object by entering paramaters for your desired type and either artist, song, or genre.
```python
import pyechonest.playlist.Playlist
p = Playlist(type='artist-radio', artist=['led zeppelin', 'rolling stones'])
```

**Code Explanation**

The program I created with the playlist is fairly straightforward, it creates an artist-radio type playlist based off of Led Zeppelin and The Rolling Stones and it prints off the name of every song in the playlist. I first initialize a new playlist object using the paramaters previously mentioned, then I use a for-each loop to print the title of each song in the playlist to the console.
```python
collect = []
    p = playlist.static(type='artist-radio', artist=['led zeppelin', 'rolling stones'])
    for song in p:
        print song.title
```

[Playlist API]: http://echonest.github.io/remix/apidocs/pyechonest.playlist.Playlist-class.html
[The Echonest Playlisting Overview]: http://developer.echonest.com/docs/v4/playlisting.html
[The Echonest Standard Playlisting]: http://developer.echonest.com/docs/v4/standard.html
[Taste Profile]: http://developer.echonest.com/docs/v4/catalog.html
