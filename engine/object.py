import pygame


class Object:

    img = None
    width = 0
    height = 0
    posX = 0
    posY = 0

    def __init__(self, imgPath, x, y):
        self.img = pygame.image.load(imgPath)
        self.width = self.img.get_rect()[2]
        self.height = self.img.get_rect()[3]
        self.posX = x
        self.posY = y

    def render(self, screen):
        screen.blit(self.img, (self.posX, self.posY))

    def checkCollision(self, obj):
        selfRect = self.img.get_rect().copy()
        selfRect = selfRect.move(self.posX, self.posY)
        objRect = obj.img.get_rect().copy()
        objRect = objRect.move(obj.posX, obj.posY)
        return selfRect.colliderect(objRect)
