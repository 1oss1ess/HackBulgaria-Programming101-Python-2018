import datetime
import random
import json

# from prettytable import PrettyTable
from song import Song


class Playlist(Song):
    def __init__(self, name, repeat=False, shuffle=False):
        assert isinstance(repeat, bool)
        assert isinstance(shuffle, bool)
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.array_of_songs = []
        self.__play_song = set()

    def __str__(self):
        return super()

    def add_song(self, song):
        if isinstance(song, Song):
            self.array_of_songs.append(song)
        else:
            raise TypeError('This argument is not a Song object!')

    def remove_song(self, song):
        if isinstance(song, Song):
            self.array_of_songs.remove(song)
        else:
            raise TypeError('This argument is not a Song object!')

    def add_songs(self, songs):
        for song in songs:
            if isinstance(song, Song):
                self.add_song(song)
            else:
                raise TypeError('This argument is not a Song object!')

    def total_length(self):
        sum_length = sum(song.length(seconds=True) for song in self.array_of_songs)
        return str(datetime.timedelta(seconds=sum_length))

    def artists(self):
        artist_songs = {}
        for song in self.array_of_songs:
            if song.artist in artist_songs:
                artist_songs[song.artist] += 1
            else:
                artist_songs[song.artist] = 1
        return artist_songs

    def __shuffle_songs(self):
        while True:
            index = random.randint(0, len(self.array_of_songs) - 1)
            if index not in self.__play_song:
                self.__play_song.add(index)
                break
            elif len(self.__play_song) == len(self.array_of_songs):
                self.__play_song.clear()
                self.__play_song.add(index)
                break
        return self.array_of_songs[index]

    def __repeat_songs(self):
        index = 0
        while True:
            if index not in self.__play_song:
                self.__play_song.add(index)
                break
            elif len(self.__play_song) == len(self.array_of_songs):
                self.__play_song.clear()
                self.__play_song.add(index)
                break
            index += 1
        return self.array_of_songs[index]

    def next_song(self):
        if not self.array_of_songs:
            raise Exception('Playlist is empty!')
        elif self.shuffle:
            return self.__shuffle_songs()
        elif self.repeat:
            return self.__repeat_songs()
        else:
            index = 0
            while True:
                if index not in self.__play_song:
                    self.__play_song.add(index)
                    break
                elif len(self.__play_song) == len(self.array_of_songs):
                    raise Exception('No more songs in playlist!')
                index += 1
            return self.array_of_songs[index]

    def __find_dashes(self):
        artist = []
        title = []
        songs = []
        for song in self.array_of_songs:
            artist.append(song.artist)
            title.append(song.title)
            songs.append(song.song_length)

        artist_max_len = len(max(artist, key=lambda s: (len(s), s)))
        title_max_len = len(max(title, key=lambda s: (len(s), s)))
        song_max_len = len(max(songs, key=lambda s: (len(s), s)))
        if song_max_len < len('Length'):
            song_max_len = len('Length')
        if artist_max_len < len('Artist'):
            artist_max_len = len('Artist')
        if title_max_len < len('Song'):
            title_max_len = len('Song')

        return artist_max_len, title_max_len, song_max_len

    def __create_table(self):
        artist_max_dashes, title_max_dashes, song_max_dashes = self.__find_dashes()
        table = '| Artist '.ljust(artist_max_dashes) + ' | Song '.ljust(title_max_dashes + 4) + '| Length '.ljust(song_max_dashes) + '|\n'
        table += '| ' + '-' * (artist_max_dashes + 1) + '|' + '-' * (title_max_dashes + 2) + '|' + '-' * (song_max_dashes + 2) + '|\n'
        for song in self.array_of_songs:
            table += '| ' + song.artist.ljust(artist_max_dashes) + ' | ' + song.title.ljust(title_max_dashes) + ' | ' + song.song_length.ljust(song_max_dashes) + ' |\n'
        return table

    def pprint_playlist(self):
        print(self.__create_table())

        # other solution for print table
        # table = PrettyTable()
        # table.field_names = ['Artist', 'Song', 'Length']

        # for song in self.array_of_songs:
        #     table.add_row([song.artist, song.title, song.length()])

        # print(table)

    def __prepare_json(self):
        data_dict = {
            'name': self.name,
            'repeat': self.repeat,
            'shuffle': self.shuffle,
            'songs': [song.__dict__ for song in self.array_of_songs],
        }

        return data_dict

    def save(self):
        json_file_name = self.name.replace(' ', '-') + '.json'

        with open(json_file_name, 'w') as f:
            f.write(json.dumps(self.__prepare_json(), indent=4))

    @staticmethod
    def load(json_text_name):
        with open(json_text_name, 'r') as f:
            load_json_file = json.load(f)
            playlist_songs = Playlist(load_json_file['name'], load_json_file['repeat'], load_json_file['shuffle'])
            for song in load_json_file['songs']:
                load_songs = Song(song['title'], song['artist'], song['album'], song['song_length'])
                playlist_songs.add_song(load_songs)
            return playlist_songs
