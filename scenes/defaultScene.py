import pygame
from pygame.math import Vector2
from scenes.scene import Scene
from scenes.character import Player
from physics.world import World
from physics.body import Body

class DefaultScene(Scene):

    def start(self):
        self.character1 = Player(pygame.Vector2(0, 0))
        self.character2 = Player(pygame.Vector2(0, 100))
        self.world = World(Vector2(0, 0))

        self.character1.control = True

        self.world.addBody(self.character1)
        self.world.addBody(self.character2)
        self.world.addBody(Body(pygame.Vector2(300, 300), 'rect', pygame.Vector2(60, 40), 'static'))
        pass

    def input(self, event):
        self.character1.input(event)
        self.character2.input(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.character1.control = not self.character1.control
                self.character2.control = not self.character2.control
        pass

    def update(self, delta):
        self.character1.update(delta)
        self.character2.update(delta)
        self.world.update(delta)
        pass

    def render(self, renderer):
        self.character1.render(renderer)
        self.character2.render(renderer)
        self.world.render(renderer)
        pass