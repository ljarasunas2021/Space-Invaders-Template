import pygame


class Text:

    def __init__(self, text, xPosition=0, yPosition=0, size=32, textColor=(255, 255, 255), fontType='freesansbold.ttf'):
        self.posX = xPosition
        self.posY = yPosition
        self.size = size
        self.textColor = textColor
        self.fontType = fontType

        self.font = pygame.font.Font(self.fontType, self.size)
        self.text = self.font.render(text, True, self.textColor)

    def render(self, screen):
        screen.blit(self.text, (self.posX, self.posY))
