import pygame


class Engine:

    def __init__(self):
        pygame.init()

    def create_screen(self, res_width, res_height):
        return pygame.display.set_mode((res_width, res_height))

    def set_name(self, name):
        pygame.display.set_caption(name)

    def get_events(self):
        return pygame.event.get()

    def update_display(self):
        pygame.display.update()
