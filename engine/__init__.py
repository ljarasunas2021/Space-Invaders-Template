import pygame
from object import Object


class Engine:

    def __init__(self):

        self.key_down_handlers = {}
        self.key_up_handlers = {}
        self.mouse_handlers = {}
        self.key_pressed_handlers = {}
        self.keys = set()
        self.background = None
        self.objects = []

        pygame.init()

    def start(self, update):
        running = True
        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type in self.mouse_handlers:
                    pos = pygame.mouse.get_pos()
                    self.mouse_handlers[event.type](pos[0], pos[1])

                if event.type == pygame.KEYDOWN:
                    self.keys.add(event.key)
                    if event.key in self.key_pressed_handlers:
                        self.key_pressed_handlers[event.key]()

                if event.type == pygame.KEYUP:
                    if event.key in self.keys:
                        self.keys.remove(event.key)

                    if event.key in self.key_up_handlers:
                        self.key_up_handlers[event.key]()

            for key in self.keys:
                if key in self.key_down_handlers:
                    self.key_down_handlers[key]()

            if self.background != None:
                self.background.render(self.screen)

            update()

            for object in self.objects:
                object.render(self.screen)

            pygame.display.update()

    def on_key_down(self, key, handler):
        self.key_down_handlers[key] = handler

    def on_key_up(self, key, handler):
        self.key_up_handlers[key] = handler

    def on_key_pressed(self, key, handler):
        self.key_pressed_handlers[key] = handler

    def on_mouse_move(self, handler):
        self.mouse_handlers[pygame.MOUSEMOTION] = handler

    def on_mouse_click(self, handler):
        self.mouse_handlers[pygame.MOUSEBUTTONDOWN] = handler

    def create_screen(self, res_width, res_height):
        return pygame.display.set_mode((res_width, res_height))

    def set_name(self, name):
        pygame.display.set_caption(name)

    def set_background(self, engine, background_path, screen):
        self.background = Object(engine, background_path, 0, 0)
        self.screen = screen

    def add_object(self, object):
        self.objects.append(object)

    def remove_object(self, object):
        if object in self.objects:
            self.objects.remove(object)
