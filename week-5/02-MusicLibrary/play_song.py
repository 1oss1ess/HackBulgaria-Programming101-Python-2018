from pygame import *

mixer.pre_init(44100, 16, 2, 4096)
mixer.init()
mixer.music.load('/home/rampage/Music/Warriors Of The World lyrics.mp3')
mixer.music.set_volume(0.5)
mixer.music.play()
while mixer.music.get_busy():
    time.Clock().tick(10)
