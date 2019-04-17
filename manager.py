import sys, pygame
from scenes.defaultScene import DefaultScene

class Manager:

    def __init__(self):
        self.all_scenes = []
        self.index = 0
        self.all_scenes.append(DefaultScene(self))
    
    def start(self):
        self.all_scenes[self.index].start()
        pass

    def input(self, keys):
        self.all_scenes[self.index].input(keys)
        pass

    def update(self, delta):
        self.all_scenes[self.index].update(delta)
        pass

    def render(self, renderer):
        self.all_scenes[self.index].render(renderer)
        pass