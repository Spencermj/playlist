## playlist

Create a playlist using Pyechonest

**What It Does**

Using [Playlist API], you can create an ordered list of tracks when given certain paramaters. [The Echonest] goes in depth on what you can do with each of the methods in the API and how the playlist changes with each paramater. The Echonest also has guides on how to perform basic, standard, and premium playlisting. Using the playlist API, you can make a very basic playlist with a small amount of code or you can make a very advanced playlist.

**Dependencies**

You will need Pyechonest to use playlist.py.

**How To Create A Playlist**

There are many different paramaters that will affect the outcome of the playlist. To make a basic playlist, the only paramaters necessary are anywhere from one to five artists, genres, or songs and a playlist type. The following is a list of playlist types:

    artist-radio - Plays songs from the given artist(s) and similar artists.
    song-radio - Plays songs similar to the given song(s).
    genre-radio - Plays songs from artists relevant to the given genre.
    artist - Plays songs from only the given artist(s).
    catalog - Plays songs listed in the given Taste Profile.
    catalog-radio - Plays songs listed in the given Taste Profile, as well as similar artists and songs outside of the Taste
    Profile.

With all the playlist types other than Catalog and Catalog-Radio, you can specify an attribute that will determine what songs are added to the playlist. Some of the allowed attributes include song hotttnesss, tempo, duration, loudness, mode, key, energy, and danceability. To provide more variety in a playlist, the limited_interactivity paramater can be set to true to cause the playlist to obey the following conditions:

    No more than 2 songs in a row from the same album
    No more than 3 songs from an album in a 3 hour period
    No more than 3 different songs in a row by the same artist
    No more than 4 songs by the same artist in a 3 hour period
    
The Catalog and Catalog-Radio playlist types are used when you are creating a playlist based off a Taste Profile, as described below.

**Example**

Simply initialize the aqplayer with an 'echonest.remix.audio.LocalAudioFile'.
Then you can feed it any type of AudioQuantum to be played.
```python
code
```

**Code Explanation**

In the initializer, aqplayer first creates a pyaudio object. It then retrieves the wave file associated with the 'echonest.remix.audio.LocalAudioFile' and opens it using the built in wave module. After opening the wave, a stream is opened using the pyaudio object. The parameters used to open the stream are retrieved from the wave file.
```python
code
```
To find the start of the wave frames to be fed to the stream, aqplayer multiplies the starting time of the 'echonest.remix.audio.AudioQuantum' by the wave framerate. To calculate the number of frames, aqplayer multiplies the duration of the 'echonest.remix.audio.AudioQuantum' by the wave framerate. After these values are found, the position of the wave is set, and the frames read using wave's readframes method. These frames are written to the stream to be played.
```python
code
```
Make sure to close the pyaudio stream when you are done by calling the closeStream() method.
