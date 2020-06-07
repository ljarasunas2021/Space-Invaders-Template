import pygame
from pygame import mixer


class Audio:

    def __init__(self, path, isBackgroundMusic, volume):
        if isBackgroundMusic:
            mixer.music.load(path)
            mixer.music.set_volume(volume)
            mixer.music.play(-1)
        else:
            sound = mixer.Sound(path)
            sound.set_volume(volume)
            sound.play()
