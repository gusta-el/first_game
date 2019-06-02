import pygame
from pygame.math import Vector2
from pygame import Rect
from scenes.scene import Scene

class OptionScene(Scene):

    def __init__(self, manager):
        self.manager = manager

    def start(self):
        self.menu_op = pygame.image.load("res/op_scene.jpg")
        pass

    def input(self, event):
        pass

    def update(self, delta):
        pass

    def render(self, renderer):
        pass

