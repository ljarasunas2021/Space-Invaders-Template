import pygame


class Text:

    def __init__(self, text, x_position=0, y_position=0, size=32, text_color=(255, 255, 255), font_type='freesansbold.ttf'):
        self.posX = x_position
        self.posY = y_position
        self.size = size
        self.text_color = text_color
        self.font_type = font_type

        self.font = pygame.font.Font(self.font_type, self.size)
        self.text = self.font.render(text, True, self.text_color)

    def render(self, screen):
        screen.blit(self.text, (self.posX, self.posY))
