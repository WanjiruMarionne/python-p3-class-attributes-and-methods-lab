#!/usr/bin/env python3

class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_to_genres(cls, genre):
        if cls.genres.count(genre) == 0:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if cls.artists.count(artist) == 0:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre) is None:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist) is None:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1