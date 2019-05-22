import pygame
from pygame.math import Vector2

class Body:

    #Position -> pygame.Vector2()
    #Shape -> 'rect' ou 'circle'
    #Size -> pygame.Vector2(), caso for retangulo, raio numerico, caso for circulo
    #BodyType -> 'static' ou 'dynamic'

    def __init__(self, position, shape, size, bodyType):
        self.position = position
        self.velocity = Vector2(0, 0)
        self.shape = shape
        self.size = size
        self.bodyType = bodyType

        if self.shape != 'rect' and self.shape != 'circle':
            print("ERRO, corpo não pode ser do formato '" + self.shape + "', deve ser 'rect' ou 'circle'")

    def render(self, renderer):
        if self.bodyType == 'static':
            renderer.setColor(150, 0, 0, 255)
        elif self.bodyType == 'dynamic':
            renderer.setColor(0, 100, 0, 255)
            
        if self.shape == 'rect':
            renderer.drawRect(self.position.x - self.size.x/2, self.position.y - self.size.y/2, self.size.x, self.size.y)
        elif self.shape == 'circle':
            renderer.drawCircle(int(self.position.x), int(self.position.y), int(self.size))

    def collide(self, other):
        return True

    def minX(self):
        return self.position.x - self.size.x/2

    def maxX(self):
        return self.position.x + self.size.x/2

    def minY(self):
        return self.position.y - self.size.y/2
    
    def maxY(self):
        return self.position.y + self.size.y/2