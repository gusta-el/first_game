import pygame
from pygame.math import Vector2
from objects.gameobject import GameObject

class Concerto(GameObject):

    def __init__(self, obj, defaultScene):
        super().__init__()
        self.obj = obj
        self.defaultScene = defaultScene
        self.red = pygame.Color(255, 0, 0)
        self.blue = pygame.Color(0, 0, 255)
        self.fix = 0

    def update(self, delta):
        self.z = self.obj.y - 16 + self.obj.height/2    
        
        if self.defaultScene.currentCharacter.ferramenta != None:
            if self.defaultScene.currentCharacter.ferramenta.type[2:] == self.obj.type[2:]:

                cor = self.red

                if self.defaultScene.currentCharacter.acting:
                    thispos = Vector2(self.obj.x, self.obj.y)
                    if (thispos - self.defaultScene.currentCharacter.position).length() < 64:
                        self.fix += delta
                        cor = self.blue
                        if self.fix > 1:
                            self.defaultScene.removeObject(self)
                            self.defaultScene.score += 1
                            if self.defaultScene.score == self.defaultScene.total_concertos:
                                #Mapa concluido, faz transição
                                
                                self.defaultScene.completeLevel()
                            fixed = pygame.mixer.Sound("res/sounds/fixed.wav")
                            pygame.mixer.Sound.play(fixed)
                else:
                    self.fix = 0

                self.defaultScene.addParticle(Vector2(self.obj.x, self.obj.y), cor)

        pass

    def render(self, renderer):
        renderer.drawTexture(self.obj.image, self.obj.x - 16 + self.obj.width/2, self.obj.y - 16 + self.obj.height/2)

        pass

    def input(self, event):
        pass