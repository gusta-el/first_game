import sys, pygame
from scenes.defaultScene import DefaultScene
from scenes.menuScene import MenuScene

class Manager:

    def __init__(self):
        self.all_scenes = []
        self.index = 0
        self.all_scenes.append(MenuScene(self)) #0
        self.all_scenes.append(DefaultScene(self)) #1
    
    def changeState(self, index):
        self.index = index
        self.start()

    def start(self):
        self.all_scenes[self.index].start()
        pass

    def input(self, event):
        self.all_scenes[self.index].input(event)
        pass

    def update(self, delta):
        self.all_scenes[self.index].update(delta)
        pass

    def render(self, renderer):
        self.all_scenes[self.index].render(renderer)
        pass