import datetime


class Song:
    def __init__(self, title, artist, album, song_length):
        self.title = title
        self.artist = artist
        self.album = album
        self.song_length = song_length
        self.__check_time_song_is_valid(song_length)

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.song_length)

    def __eq__(self, other):
        return (
            self.title == other.title
            and self.artist == other.artist
            and self.album == other.album
            and self.song_length == other.song_length
        )

    def __hash__(self):
        return hash((self.title, self.artist, self.album, self.song_length))

    def __check_time_song_is_valid(self, song_time):
        timeformat = "%H:%M:%S"
        zero = '0:'
        if len(song_time.split(':')) == 3:
            try:
                datetime.datetime.strptime(song_time, timeformat)
            except ValueError:
                raise('Oops!  That was no valid time.  Try again...')
        elif len(song_time.split(':')) == 2:
            try:
                datetime.datetime.strptime(zero + song_time, timeformat)
            except ValueError:
                raise('Oops!  That was no valid time.  Try again...')
        elif len(song_time.split(':')) == 1:
            try:
                datetime.datetime.strptime(zero + zero + song_time, timeformat)
            except ValueError:
                raise('Oops!  That was no valid time.  Try again...')
        else:
            raise('Oops!  That was no valid time.  Try again...')

    def length(self, **kwargs):
        if len(kwargs) > 1:
            raise ValueError('Bad command. Try again...')
        split_song = self.song_length.split(':')
        for key, value in kwargs.items():
            if key == 'seconds':
                if len(split_song) == 1:
                    return int(split_song[0])
                elif len(split_song) == 2:
                    return int(split_song[0]) * 60 + int(split_song[1])
                else:
                    return int(split_song[0]) * 3600 + int(split_song[1]) * 60 + int(split_song[2])
            elif key == 'minutes':
                if len(split_song) == 1:
                    return 0
                elif len(split_song) == 2:
                    return int(split_song[0])
                else:
                    return int(split_song[0]) * 60 + int(split_song[1])
            elif key == 'hours':
                if len(split_song) == 3:
                    return int(split_song[0])
                else:
                    return 0

        return len(self.song_length)
