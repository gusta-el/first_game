import pygame
from objects.gameobject import GameObject
import math

class Ferramenta(GameObject):

    def __init__(self, obj, defaultScene):
        super().__init__()
        self.obj = obj
        self.defaultScene = defaultScene
        self.close = False
        self.timer = 0

    def update(self, delta):
        self.timer += delta
        self.z = self.obj.y - 16 + self.obj.height/2
        pos = pygame.Vector2(self.obj.x - 16 + self.obj.width/2, self.obj.y - 16 + self.obj.height/2)
        self.close = (self.defaultScene.currentCharacter.position - pos).length() < 32
        pass

    def render(self, renderer):
        renderer.drawTexture(
            self.obj.image,
            self.obj.x - 16 + self.obj.width/2,
            self.obj.y - 16 + self.obj.height/2, scale=(1 if not self.close else 1 + math.sin(self.timer*5) * 0.2))
        pass

    def input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if self.close and self.defaultScene.currentCharacter.ferramenta == None:
                    fixed = pygame.mixer.Sound("res/sounds/catchTool.wav")
                    pygame.mixer.Sound.play(fixed)
                    self.defaultScene.currentCharacter.ferramenta = self.obj
                    self.defaultScene.removeObject(self)
        pass