import pygame
import pybox2d
from scenes.scene import Scene
from scenes.character import Player

class DefaultScene(Scene):

    def start(self):
        self.character = Player()

        self.world = b2World()
        pass

    def input(self, event):
        self.character.input(event)
        pass

    def update(self, delta):
        self.character.update(delta)
        pass

    def render(self, renderer):
        self.character.render(renderer)
        pass