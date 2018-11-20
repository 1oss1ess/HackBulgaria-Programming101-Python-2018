import mutagen
import os
import datetime

from song import Song
from playlist import Playlist


class MusicCrawler:
    def __init__(self, path):
        self.path = path

    def __check_song(self, song_info):
        song_dict = {}
        if 'TPE1' in song_info:
            song_dict['artist'] = song_info['TPE1'].text[0]
        else:
            song_dict['artist'] = 'Unknown Artist'
        if 'TALB' in song_info:
            song_dict['album'] = song_info["TALB"].text[0]
        else:
            song_dict['album'] = 'Unknown Album'
        if 'TIT2' in song_info:
            song_dict['title'] = song_info['TIT2'].text[0]
        else:
            song_dict['title'] = 'Unknown Title'
        if song_info.info.length is not None:
            song_dict['length'] = str(datetime.timedelta(seconds=song_info.info.length // 1))[2:]
        else:
            song_dict['length'] = 'Unknown Length'

        return song_dict

    def generate_playlist(self):
        array = self.path.split('/')
        name_of_playlist = array[-2]
        playlist = Playlist(name_of_playlist)
        songs = [mp3 for mp3 in os.listdir(self.path) if mp3.endswith('.mp3')]
        for song in songs:
            info_song = mutagen.File(self.path + "/" + song)
            info = self.__check_song(info_song)
            new_song = Song(
                artist=info['artist'], title=info['title'], album=info['album'], song_length=info['length'])
            playlist.add_song(new_song)

        return playlist


crawler = MusicCrawler("/home/rampage/Music/")
playlist = crawler.generate_playlist()
playlist.pprint_playlist()
