from pytest_bdd import scenario, given, when, then
from bididi import Album, Artist, Song, SongPublisher, SongCollection, SongPlayer
from datetime import datetime
import pytest


@scenario("publish_song.feature", "Publish the song")
def test_publish():
    pass

@scenario("publish_song.feature", "Play a song")
def test_play():
    pass

@pytest.fixture
def album():
    return Album("Album de prueba", 2023)


@pytest.fixture
def artist():
    return Artist("Artista de prueba")


@given("I have a song", target_fixture="song")
def song(artist, album):
    return Song("cancion A", artist, datetime.now(), 3.5*60, "Letra por letra", album )


@when("I publish the song")
def publish(song):
    SongPublisher.publish_song(song)


@when("I play the song")
def play_song(song):
    SongPlayer.play_song(song)


@then("I have a song in collection")
def song_in_collection(song):
    collection = SongCollection()
    songs = collection.read_collection()
    assert len(songs)
    last = songs.pop()
    assert song.title == last.title


@then("the times listened increases")
def increase_counter(song):
    assert song.times_listened > 0