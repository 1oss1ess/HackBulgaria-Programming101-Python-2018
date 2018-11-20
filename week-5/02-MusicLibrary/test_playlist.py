import unittest

from song import Song
from playlist import Playlist


class TestPlayList(unittest.TestCase):
    def setUp(self):
        self.code_songs = Playlist(name="Code", repeat=True, shuffle=True)
        self.song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", song_length="0:44")
        self.song2 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", song_length="1:33")
        self.song3 = Song(title="Warriors Of The World", artist="Manowar", album="The Sons of Warrior", song_length="5:55")
        self.song4 = Song(title="The World", artist="Manowar", album="The Sons of World", song_length="1:50:55")
        self.arr_songs = [self.song2, self.song3]
        self.code_songs.add_song(self.song1)

    def test_constructor(self):
        self.assertTrue(isinstance(self.code_songs, Playlist))

    def test_initialization_with_invalid_attributes(self):
        with self.subTest('repeat is not bool'):
            self.setUp()
            with self.assertRaises(AssertionError):
                Playlist(name='asd', repeat=1, shuffle=True)

        with self.subTest('shuffle is not bool'):
            self.setUp()
            with self.assertRaises(AssertionError):
                Playlist(name='asd', repeat=True, shuffle=1)

    def test_add_song(self):
        self.assertTrue(self.song1 in self.code_songs.array_of_songs)

    def test_add_song_with_invalid_data(self):
        self.setUp()
        with self.assertRaises(TypeError):
            self.code_songs.add_song('Manowar')

    def test_remove_song(self):
        self.code_songs.add_song(self.song2)
        self.assertTrue(self.song1 in self.code_songs.array_of_songs)
        self.code_songs.remove_song(self.song2)
        self.assertFalse(self.song2 in self.code_songs.array_of_songs)

    def test_remove_song_with_invalid_data(self):
        self.setUp()
        with self.assertRaises(TypeError):
            self.code_songs.remove_song('Manowar')

    def test_add_arr_of_songs(self):
        self.code_songs.add_songs(self.arr_songs)
        self.assertTrue(self.song2 in self.code_songs.array_of_songs)
        self.assertTrue(self.song3 in self.code_songs.array_of_songs)

    def test_total_length_sec(self):
        self.code_songs = Playlist('name')
        self.code_songs.add_song(self.song1)
        self.assertEqual(self.code_songs.total_length(), '0:00:44')

    def test_total_length_minutes(self):
        self.code_songs = Playlist('name')
        self.code_songs.add_song(self.song2)
        self.code_songs.add_song(self.song3)
        self.assertEqual(self.code_songs.total_length(), '0:07:28')

    def test_total_length_hours(self):
        self.code_songs = Playlist('name')
        self.code_songs.add_song(self.song1)
        self.code_songs.add_song(self.song2)
        self.code_songs.add_song(self.song3)
        self.code_songs.add_song(self.song4)
        self.assertEqual(self.code_songs.total_length(), '1:59:07')

    def test_artist(self):
        self.code_songs = Playlist('name')
        s = Song(title='Superman', artist='Eminem', album='???', song_length='6:36')
        self.code_songs.add_song(self.song1)
        self.code_songs.add_song(self.song2)
        self.code_songs.add_song(s)

        expected_data = {
            'Manowar': 2,
            'Eminem': 1,
        }

        result_data = self.code_songs.artists()
        self.assertEqual(result_data, expected_data)

    def test_next_song_playlist_is_empty(self):
        self.code_songs = Playlist('name')
        with self.assertRaises(Exception):
            self.code_songs.next_song()

    def test_repeat_songs(self):
        self.code_songs = Playlist('name', repeat=True)
        self.code_songs.add_song(self.song1)
        self.code_songs.add_song(self.song2)
        self.code_songs.add_song(self.song3)

        current_song = self.code_songs.next_song()
        self.assertEqual(current_song, self.song1)

        current_song = self.code_songs.next_song()
        self.assertEqual(current_song, self.song2)

        current_song = self.code_songs.next_song()
        self.assertEqual(current_song, self.song3)

        current_song = self.code_songs.next_song()
        self.assertEqual(current_song, self.song1)

    def test_shuffle_songs(self):
        self.code_songs = Playlist('name', shuffle=True)
        self.code_songs.add_song(self.song1)
        self.code_songs.add_song(self.song2)
        self.code_songs.add_song(self.song3)
        array_of_current_songs = [self.song1, self.song2, self.song3, self.song1, self.song2, self.song3]
        array_of_next_songs = []
        array_of_next_songs.append(self.code_songs.next_song())
        array_of_next_songs.append(self.code_songs.next_song())
        array_of_next_songs.append(self.code_songs.next_song())
        array_of_next_songs.append(self.code_songs.next_song())
        array_of_next_songs.append(self.code_songs.next_song())
        array_of_next_songs.append(self.code_songs.next_song())

        self.assertNotEqual(array_of_current_songs, array_of_next_songs)

    def test_load_playlist(self):
        self.code_songs = Playlist('my playlist')
        self.code_songs.add_song(self.song1)
        self.code_songs.add_song(self.song2)
        self.code_songs.add_song(self.song3)
        self.code_songs.add_song(self.song4)
        self.code_songs.save()
        load_playlist = Playlist.load('my-playlist.json')
        self.assertEqual(load_playlist.name, 'my playlist')
        self.assertFalse(load_playlist.shuffle)
        self.assertFalse(load_playlist.repeat)


if __name__ == "__main__":
    unittest.main()
