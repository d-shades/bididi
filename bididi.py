from dataclasses import dataclass
from datetime import datetime
import pickle


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

    def play(self):
        self.times_listened += 1
        self.artist.times_listened += 1


class SongCollection:
    """
    Store songs.
    """
    def __init__(self) -> None:
        self.collection = []

    def save_collection(self):
        with open("collection.pkl", "wb") as io:
            pickle.dump(self.collection, io)

    def read_collection(self):
        with open("collection.pkl", "rb") as io:
            return pickle.load(io, encoding="utf-8")

    def add_to_collection(self, song):
        self.collection.append(song)


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
    def publish_song(cls, song: Song) -> None:
        collection = SongCollection()
        collection.add_to_collection(song)
        collection.save_collection()


class SongPlayer:

    @classmethod
    def play_song(cls, song):
        song.play()

if __name__ == "__main__":
    # example
    pass