import pygame
from pygame.math import Vector2
from objects.gameobject import GameObject

class Particle(GameObject):

    def __init__(self,  position, velocity, gravity, size, cor, defaultScene):
        super().__init__()
        self.position = position
        self.velocity = velocity
        self.gravity = gravity
        self.size = size
        self.cor = cor
        self.life = 1
        self.defaultScene = defaultScene
        self.drag = 0.99

    def update(self, delta):

        self.velocity *= self.drag
        self.velocity += self.gravity
        self.position += self.velocity
        self.z = -1000
        self.life -= delta

        if self.life <= 0:
            self.defaultScene.removeObject(self)
        pass

    def render(self, renderer):
        renderer.setColor(self.cor.r, self.cor.g, self.cor.b, int(self.life * 255))
        renderer.fillCircle(int(self.position.x), int(self.position.y), int(self.size))
        pass

    def input(self, event):
        pass