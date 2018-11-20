import unittest
from song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='3:44')
        self.equal_song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='3:44')
        self.different_song = Song(title='Warrior', artist='Manowar', album='The Sons of Warrior', song_length='5:33')

    def test_to_str(self):
        self.assertEqual(str(self.song), 'Manowar - Odin from The Sons of Odin - 3:44')

    def test_eq_true(self):
        self.assertTrue(self.song == self.equal_song)

    def test_eq_false(self):
        self.assertFalse(self.song == self.different_song)

    def test_hash(self):
        self.assertTrue(isinstance(hash(self.song), int))

    def test_creating_song_with_invalid_length(self):
        with self.assertRaises(Exception):
            Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='60')

        with self.assertRaises(Exception):
            Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='60:59')

        with self.assertRaises(Exception):
            Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='24:0:0')

        with self.assertRaises(Exception):
            Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='23:59:5a')

        with self.assertRaises(Exception):
            Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='0:0:0:0')

    def test_length_seconds_true(self):
        song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='59')
        self.assertEqual(song.length(seconds=True), 59)

        song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='1:59')
        self.assertEqual(song.length(seconds=True), 119)

        song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='1:1:59')
        self.assertEqual(song.length(seconds=True), 3719)

    def test_length_minutes_true(self):
        song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='0:59')
        self.assertEqual(song.length(minutes=True), 0)

        song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='1:59')
        self.assertEqual(song.length(minutes=True), 1)

        song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='1:1:59')
        self.assertEqual(song.length(minutes=True), 61)

        song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='59:00')
        self.assertEqual(song.length(minutes=True), 59)

    def test_length_hours_true(self):
        song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='0:59')
        self.assertEqual(song.length(hours=True), 0)

        song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='0:0:1')
        self.assertEqual(song.length(hours=True), 0)

        song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='1:0:0')
        self.assertEqual(song.length(hours=True), 1)

        song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='23:59:59')
        self.assertEqual(song.length(hours=True), 23)

    def test_length_with_invalid_comand(self):
        song = Song(title='Odin', artist='Manowar', album='The Sons of Odin', song_length='3:44')

        with self.assertRaises(Exception):
            song.length(seconds=True, minutes=True, hours=True)

        with self.assertRaises(Exception):
            song.length(seconds=True, minutes=True)

        with self.assertRaises(Exception):
            song.length(seconds=True, hours=True)

        with self.assertRaises(Exception):
            song.length(minutes=True, hours=True)


if __name__ == '__main__':
    unittest.main()
