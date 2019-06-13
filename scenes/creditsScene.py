import pygame
from pygame.math import Vector2
from pygame import Rect
from scenes.scene import Scene

class CreditsScene (Scene):
    
    def __init__(self, manager):
        super().__init__(manager)

    def start(self):
        
        self.credits = pygame.image.load("res/credits.png")
        self.alpha = 1
        self.screen_size = Vector2(pygame.screen_size[0], pygame.screen_size[1])
        self.zero = Vector2(self.screen_size.x/2, self.screen_size.y/2)

        self.intro = True
        self.outro = False

    def input(self, event):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.outro = True
            self.intro = False
            pass


    def update(self, delta):
        if self.intro:
            self.alpha -= delta
            if self.alpha <= 0:
                self.alpha = 0
                self.intro = False
                #Terminou a intro
        elif self.outro:
            self.alpha += delta
            if self.alpha >= 1:
                self.alpha = 1
                self.outro = False
                self.manager.changeState("Menu")

        pass

    def render(self, renderer):
       
        renderer.camera_pos = Vector2(0, 0)
        renderer.drawTexture(self.credits, 0, 0, pygame.screen_size[0], pygame.screen_size[1])

        #Desenha o fade in/out
        renderer.camera_pos = self.zero
        renderer.startShape()
        renderer.setColor(0, 0, 0, int(self.alpha * 255))
        renderer.fillRect(0, 0, self.screen_size.x, self.screen_size.y)
        renderer.endShape()        
        pass



