import pygame
import pygame
from pygame.math import Vector2

class Player:

    def __init__(self):
        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.texture = pygame.image.load("res/character.png")

        self.speed = 5
        self.hor = 0
        self.ver = 0
        pass

    def render(self, renderer):
        renderer.drawTexture(self.texture, self.position[0], self.position[1], 64, 64)
        pass

    def update(self, delta):
        self.position += self.velocity

        if self.hor != 0 or self.ver != 0:
            tvel = Vector2(self.hor, self.ver).normalize() * self.speed
        else: tvel = Vector2(0, 0)

        self.velocity += (tvel - self.velocity) / 5
        pass

    def input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.hor = -1
            elif event.key == pygame.K_RIGHT:
                self.hor = 1
            elif event.key == pygame.K_UP:
                self.ver = -1
            elif event.key == pygame.K_DOWN:
                self.ver = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    self.hor = 1
                else:
                    self.hor = 0
            elif event.key == pygame.K_RIGHT:
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    self.hor = -1
                else:
                    self.hor = 0
            elif event.key == pygame.K_UP:
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    self.ver = 1
                else:
                    self.ver = 0
            elif event.key == pygame.K_DOWN:
                if pygame.key.get_pressed()[pygame.K_UP]:
                    self.ver = 1
                else:
                    self.ver = 0
        pass

