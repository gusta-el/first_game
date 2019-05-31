import pygame
from objects.gameobject import GameObject
from physics.body import Body

class MapProp(GameObject):

    def __init__(self, position, image):
        super().__init__()
        self.position = position
        self.image = image

    def update(self, delta):
        self.z = self.position.y
        pass

    def render(self, renderer):
        renderer.drawTexture(self.image, self.position.x, self.position.y, self.image.get_width(), self.image.get_height())
        pass

    def input(self, event):
        pass