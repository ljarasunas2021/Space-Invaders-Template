import pygame


class Engine:

    def __init__(self):
        pygame.init()

    def createScreen(self, resWidth, resHeight):
        return pygame.display.set_mode((resWidth, resHeight))

    def setName(self, name):
        pygame.display.set_caption(name)

    def getEvents(self):
        return pygame.event.get()

    def updateDisplay(self):
        pygame.display.update()
