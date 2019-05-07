import pygame
from pygame.math import Vector2
from scenes.scene import Scene
from scenes.character import Player
from physics.world import World
from physics.body import Body

class DefaultScene(Scene):

    def start(self):
        self.character = Player()
        self.world = World(Vector2(0, 0))

        self.world.addBody(self.character)
        pass

    def input(self, event):
        self.character.input(event)
        pass

    def update(self, delta):
        self.character.update(delta)
        self.world.update(delta)
        pass

    def render(self, renderer):
        self.character.render(renderer)
        self.world.render(renderer)
        pass