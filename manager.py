import sys, pygame
from scenes.defaultScene import DefaultScene
from scenes.menuScene import MenuScene
from scenes.optionsScene import OptionScene
from scenes.gameOverScene import GameOverScene
from scenes.levelSelectScene import LevelSelectScene
from scenes.resultScene import ResultScene

class Manager:

    def __init__(self):
        self.all_scenes = {}
        self.index = "Menu"
        self.all_scenes["Menu"] = MenuScene(self)
        self.all_scenes["Game"] = DefaultScene(self)
        self.all_scenes["Options"] = OptionScene(self)
        self.all_scenes["GameOver"] = GameOverScene(self)
        self.all_scenes["LevelSelect"] = LevelSelectScene(self)
        self.all_scenes["Result"] = ResultScene(self)

    def changeState(self, index):
        self.index = index
        self.start()

    def start(self):
        print("Iniciando cena " + str(self.all_scenes[self.index]))
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