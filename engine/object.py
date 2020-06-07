import pygame


class Object:

    img = None
    width = 0
    height = 0
    pos_x = 0
    pos_y = 0

    def __init__(self, img_path, x, y):
        self.img = pygame.image.load(img_path)
        self.width = self.img.get_rect()[2]
        self.height = self.img.get_rect()[3]
        self.pos_x = x
        self.pos_y = y

    def render(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))

    def check_collision(self, obj):
        selfRect = self.img.get_rect().copy()
        selfRect = selfRect.move(self.pos_x, self.pos_y)
        objRect = obj.img.get_rect().copy()
        objRect = objRect.move(obj.pos_x, obj.pos_y)
        return selfRect.colliderect(objRect)
