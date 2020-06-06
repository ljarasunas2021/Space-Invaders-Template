import pygame


class Engine:
    resolutionWidth = 800
    resolutionHeight = 600

    def __init__(self, resWidth, resHeight, start, update):
        self.resolutionWidth = resWidth
        self.resolutionHeight = resHeight
        start()
        update()
