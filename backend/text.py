import pygame
from engine import Engine


class Text:

    def __init__(self, text, x_position=0, y_position=0, size=32, text_color=(255, 255, 255), font_type='freesansbold.ttf'):
        self.posX = x_position
        self.posY = y_position
        self.size = size
        self.text_color = text_color
        self.font_type = font_type
        self.hidden = False

        self.font = pygame.font.Font(self.font_type, self.size)
        self.text = self.font.render(text, True, self.text_color)

        self.screen = Engine.instance.screen
        Engine.instance.add_object(self)

    def change_text(self, new_text):
        self.text = self.font.render(new_text, True, self.text_color)

    def hide(self):
        self.hidden = True

    def show(self):
        self.hidden = False

    def render(self):
        if not self.hidden:
            self.screen.blit(self.text, (self.posX, self.posY))
