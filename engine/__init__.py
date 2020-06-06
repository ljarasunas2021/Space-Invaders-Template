import pygame


class Engine:

    def __init__(self, start, update):
        pygame.init()
        start()
        update()

    def createScreen(self, resWidth, resHeight):
        return pygame.display.set_mode((resWidth, resHeight))

    def setName(self, name):
        pygame.display.set_caption(name)
