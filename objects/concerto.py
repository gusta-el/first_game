import pygame
from objects.gameobject import GameObject

class Concerto(GameObject):

    def __init__(self, obj):
        super().__init__()
        self.obj = obj

    def update(self, delta):
        self.z = self.obj.y - 16 + self.obj.height/2
        pass

    def render(self, renderer):
        renderer.drawTexture(self.obj.image, self.obj.x - 16 + self.obj.width/2, self.obj.y - 16 + self.obj.height/2)
        pass

    def input(self, event):
        pass