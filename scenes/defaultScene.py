import pygame
from scenes.scene import Scene

class DefaultScene(Scene):

    def start(self):
        self.img = pygame.image.load("res/img.png")

        self.timer = 0

        pass

    def input(self, keys):
        pass

    def update(self, delta):
        self.timer += delta * 50
        pass

    def render(self, renderer):
        renderer.drawTexture(self.img, 100, 100, 100, 100, self.timer)
        pass