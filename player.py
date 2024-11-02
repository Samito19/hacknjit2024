import time
from pygame import mixer


def play_ai_response():
    mixer.init()
    mixer.music.load("speech.mp3")
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)


