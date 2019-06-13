import pygame
from pygame.math import Vector2
from pygame import Rect
from scenes.scene import Scene

class OptionScene(Scene):

    def __init__(self, manager):
        super().__init__(manager)

    def start(self):
        self.menu_op = pygame.image.load("res/op_scene.png")
        self.alpha = 1
        self.screen_size = Vector2(pygame.screen_size[0], pygame.screen_size[1])
        self.zero = Vector2(self.screen_size.x/2, self.screen_size.y/2)

        rx = self.screen_size.x / 829
        ry = self.screen_size.y / 481

        #Botões
        self.ligar = Rect(-40*rx, -30*ry, 95*rx, 25*ry)
        self.desligar = Rect(-40*rx, 0*ry, 135*rx, 25*ry)
        self.voltar = Rect(100*rx, 72*ry, 72*rx, 20*ry)

        self.selection = self.ligar
        self.tweenSelection = {
            "x": self.selection.x,
            "y": self.selection.y,
            "width": self.selection.width,
            "height": self.selection.height
        }

        self.intro = True
        self.outro = False
        pass

    def input(self, event):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if self.selection == self.ligar:
                self.manager.sound = True
                pass
            elif self.selection == self.desligar:
                self.manager.sound = False
                pass
            elif self.selection == self.voltar:
                self.manager.changeState("Menu")
                pass

        if not self.outro:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.selection == self.ligar:
                        self.selection = self.desligar
                    elif self.selection == self.desligar:
                        self.selection = self.voltar
                if event.key == pygame.K_UP:
                    if self.selection == self.voltar:
                        self.selection = self.desligar
                    elif self.selection == self.desligar:
                        self.selection = self.ligar        
        pass


    def update(self, delta):
        
        self.tweenSelection["x"] += (self.selection.x - self.tweenSelection["x"])/5
        self.tweenSelection["y"] += (self.selection.y - self.tweenSelection["y"])/5
        self.tweenSelection["width"] += (self.selection.width - self.tweenSelection["width"])/5
        self.tweenSelection["height"] += (self.selection.height - self.tweenSelection["height"])/5

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
                #Terminou a outro

                if self.selection == self.ligar:
                    #Ligar audio
                    pass 
                elif self.selection == self.desligar:
                    #Desligar audio
                    pass
                elif self.selection == self.voltar:
                    self.manager.changeState("Menu")
                    pass

    def render(self, renderer):
       
        renderer.camera_pos = Vector2(0, 0)
        renderer.drawTexture(self.menu_op, 0, 0, pygame.screen_size[0], pygame.screen_size[1])

        renderer.setColor(255, 0, 0, 255)
        renderer.startShape()
        renderer.drawRect(self.tweenSelection["x"], self.tweenSelection["y"], self.tweenSelection["width"], self.tweenSelection["height"])
        renderer.endShape()

        #Desenha o fade in/out
        renderer.camera_pos = self.zero
        renderer.startShape()
        renderer.setColor(0, 0, 0, int(self.alpha * 255))
        renderer.fillRect(0, 0, self.screen_size.x, self.screen_size.y)
        renderer.endShape()        
        pass
