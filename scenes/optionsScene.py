import pygame
from pygame.math import Vector2
from pygame import Rect
from scenes.scene import Scene

class OptionScene(Scene):

    def __init__(self, manager):
        super().__init__(manager)

    def start(self):
        self.menu_op = pygame.image.load("res/op_scene.png")
        pass

    def input(self, event):
        pass

    def update(self, delta):
        pass

    def render(self, renderer):
        renderer.camera_pos = pygame.Vector2(0, 0)
        renderer.drawTexture(self.menu_op, 0, 0, pygame.screen_size[0], pygame.screen_size[1])
        pass

