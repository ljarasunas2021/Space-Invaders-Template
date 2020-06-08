import pygame


class Text:

    def __init__(self, engine, text, x_position=0, y_position=0, size=32, text_color=(255, 255, 255), font_type='freesansbold.ttf'):
        self.posX = x_position
        self.posY = y_position
        self.size = size
        self.text_color = text_color
        self.font_type = font_type
        self.hidden = False

        self.font = pygame.font.Font(self.font_type, self.size)
        self.text = self.font.render(text, True, self.text_color)

        engine.add_object(self)

    def change_text(self, new_text):
        self.text = self.font.render(new_text, True, self.text_color)

    def hide(self):
        self.hidden = True

    def show(self):
        self.hidden = False

    def render(self, screen):
        if not self.hidden:
            screen.blit(self.text, (self.posX, self.posY))
