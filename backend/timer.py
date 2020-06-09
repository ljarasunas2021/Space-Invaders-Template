import pygame


class Timer:

    def __init__(self, time, handler):
        self.time = time
        self.time_left = time
        self.handler = handler

    def update(self):
        from engine import Engine

        self.time_left -= Engine.instance.delta_time
        if self.time_left <= 0:
            self.handler()
            Engine.instance.remove_timer(self)
