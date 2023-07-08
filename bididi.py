from dataclasses import dataclass
from datetime import datetime


@dataclass
class Artist:
    name: str
    times_listened: int = 0


@dataclass
class Album:
    title: str
    year_published: int


@dataclass
class Song:
    title: str
    artist: Artist
    published_date: datetime
    duration: int  # seconds
    lyrics: str
    album: Album
    times_listened: int = 0


class SongCollection:
    """
    Store songs.
    """
    def __init__(self) -> None:
        self.collection = []


class SongPublisher:
    """
    Publish song in collection.
    """
    @classmethod
    def create_artist(name: str) -> Artist:
        return Artist(name) 
    
    @classmethod
    def create_album(name: str, date_published: datetime) -> Album:
        return Album(name, date_published.year)

    @classmethod
    def create_song(title: str, artist: Artist, album: Album, published_date: datetime, duration: int) -> Song:
        return Song(title, artist, published_date, duration, '', album)

    @classmethod
    def publish_song(cls,
        song_title: str, artist_name: str, album_title: str, published_date: datetime, duration: int,
    ) -> None:
        artist = cls.create_artist(artist_name)
        album = cls.create_album(album_title, published_date)
        song = cls.create_song(song_title, artist, album, published_date, duration)
