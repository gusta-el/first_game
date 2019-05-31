import pygame
from pygame.math import Vector2
from physics.body import Body
from objects.gameobject import GameObject

class Player(Body):

    def __init__(self, position):
        super().__init__(position, 'rect', pygame.Vector2(50, 14), 'dynamic')
        self.texture = pygame.image.load("res/character.png")

        self.control = False

        self.speed = 5
        self.hor = 0
        self.ver = 0
        pass

    def render(self, renderer):

        if self.control:
            renderer.camera_pos += (self.position - renderer.camera_pos) / 5

        renderer.drawTexture(self.texture, self.position.x, self.position.y - 14, 64, 64)
        super().render(renderer)

    def update(self, delta):
        self.z = self.position.y
        if (self.hor != 0 or self.ver != 0) and self.control:
            tvel = Vector2(self.hor, self.ver).normalize() * self.speed
        else: tvel = Vector2(0, 0)

        self.velocity += (tvel - self.velocity) / 5

    def input(self, event):
        if(self.control):
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

