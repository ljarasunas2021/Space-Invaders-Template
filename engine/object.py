import pygame


class Object:

    img = None
    width = 0
    height = 0
    posX = 0
    posY = 0
    screen = None

    def __init__(self, imgPath, x, y, screen):
        self.img = pygame.image.load(imgPath)
        self.width = self.img.get_rect()[2]
        self.height = self.img.get_rect()[3]
        self.posX = x
        self.posY = y
        self.screen = screen

    def render(self):
        self.screen.blit(self.img, (self.posX, self.posY))

    def checkCollision(self, obj):
        selfRect = self.img.get_rect().copy()
        selfRect = selfRect.move(self.posX, self.posY)
        objRect = obj.img.get_rect().copy()
        objRect = objRect.move(obj.posX, obj.posY)
        return selfRect.colliderect(objRect)
