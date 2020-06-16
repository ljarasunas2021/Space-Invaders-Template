import pygame
import random
from backend.engine import Engine
from backend.object import Object
from backend.text import Text
from backend.audio import Audio
from backend.button import Button

# All of the code you write will go into this file

# Here we create the engine
engine = Engine()


# This update function is called every frame
def update():
    print("Called every frame")


# Start the game, tell engine that the update function should be called every frame
engine.start(update)
