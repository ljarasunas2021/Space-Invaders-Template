import pygame
from backend.object import Object
from backend.timer import Timer


class Engine:

    instance = None
    screen = None
    delta_time = 0

    def __init__(self):

        self.timers = []
        self.key_down_handlers = {}
        self.key_up_handlers = {}
        self.mouse_handlers = {}
        self.key_pressed_handlers = {}
        self.collision_handlers = {}
        self.keys = set()
        self.background = None
        self.objects = []

        if Engine.instance is not None:
            print("Error: Can only instantiate one instance of engine")
        else:
            Engine.instance = self

        pygame.init()

    def start(self, update):
        ticks_last_frame = 0

        running = True
        while running:

            t = pygame.time.get_ticks()
            self.delta_time = (t - ticks_last_frame) / 1000.0
            ticks_last_frame = t

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

            keys_to_remove = []

            for key in self.collision_handlers.keys():
                if key[0].destroyed or key[1].destroyed:
                    keys_to_remove.append(key)
                elif key[0].check_collision(key[1]):
                    self.collision_handlers[key](key[0], key[1])

            for key in keys_to_remove:
                self.collision_handlers.pop(key)

            for timer in self.timers:
                timer.update()

            if self.background != None:
                self.background.render()

            update()

            for object in self.objects:
                object.render()

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

    def on_collision(self, obj_1, obj_2, handler):
        self.collision_handlers[(obj_1, obj_2)] = handler

    def create_screen(self, res_width, res_height):
        self.screen = pygame.display.set_mode((res_width, res_height))
        return self.screen

    def set_name(self, name):
        pygame.display.set_caption(name)

    def set_background(self, background_path):
        self.background = Object(background_path, 0, 0)

    def add_object(self, object):
        added = False
        for i in range(len(self.objects)):
            if object.render_order > self.objects[i].render_order and not added:
                self.objects.insert(i, object)
                added = True

        if not added:
            self.objects.append(object)

    def remove_object(self, object):
        self.objects.remove(object)

    def add_timer(self, time, handler):
        timer = Timer(time, handler)
        self.timers.append(timer)

    def remove_timer(self, timer):
        self.timers.remove(timer)
