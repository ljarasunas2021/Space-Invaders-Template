import pygame


class Timer:

    def __init__(self, engine, time, handler):
        self.time = time
        self.time_left = time
        self.handler = handler
        self.engine = engine

    def update(self):
        self.time_left -= self.engine.delta_time
        if self.time_left <= 0:
            self.handler()
            self.engine.remove_timer(self)
