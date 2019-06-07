import pygame
from pygame.math import Vector2
from pygame import Rect
from scenes.scene import Scene

class MenuScene(Scene):

    def __init__(self, manager):
        super().__init__(manager)


    def start(self):
        self.menu_bg = pygame.image.load("res/menu_default.jpg")
        self.alpha = 1
        self.screen_size = Vector2(pygame.screen_size[0], pygame.screen_size[1])
        self.zero = Vector2(self.screen_size.x/2, self.screen_size.y/2)

        rx = self.screen_size.x / 1280
        ry = self.screen_size.y / 843

        #Botões
        self.start = Rect(585*rx, 390*ry, 154*rx, 50*ry)
        self.options = Rect(556*rx, 447*ry, 217*rx, 55*ry)
        self.credits = Rect(559*rx, 512*ry, 211*rx, 50*ry)

        self.selection = self.start
        self.tweenSelection = {
            "x": self.selection.x,
            "y": self.selection.y,
            "width": self.selection.width,
            "height": self.selection.height
        }

        self.intro = True
        self.outro = False
        pass

    def update(self, delta):

        self.tweenSelection["x"] += (self.selection.x - self.tweenSelection["x"])/5
        self.tweenSelection["y"] += (self.selection.y - self.tweenSelection["y"])/5
        self.tweenSelection["width"] += (self.selection.width - self.tweenSelection["width"])/5
        self.tweenSelection["height"] += (self.selection.height - self.tweenSelection["height"])/5

        if self.intro:
            self.alpha -= 0.5 * delta
            if self.alpha <= 0:
                self.alpha = 0
                self.intro = False
                #Terminou a intro
        elif self.outro:
            self.alpha += 0.5 * delta
            if self.alpha >= 1:
                self.alpha = 1
                self.outro = False
                #Terminou a outro

                if self.selection == self.start:
                    self.manager.changeState(1)
                    pass #Muda pra tela de jogo
                elif self.selection == self.options:
                    self.manager.changeState(2)
                    pass #Muda pra tela de opções
                elif self.selection == self.credits:
                    pass #Muda pra tela de créditos

            
    def render(self, renderer):
        #Reseta a posição da camera
        renderer.camera_pos = self.zero

        #Desenha o fundo do menu
        renderer.drawTexture(self.menu_bg, self.screen_size.x/2, self.screen_size.y/2, int(self.screen_size.x), int(self.screen_size.y))

        #Desenha os botões de menu
        renderer.setColor(255, 0, 0, 255)
        renderer.drawRect(self.tweenSelection["x"], self.tweenSelection["y"], self.tweenSelection["width"], self.tweenSelection["height"])

        #Desenha o fade in/out
        renderer.setColor(0, 0, 0, int(self.alpha * 255))
        renderer.fillRect(0, 0, self.screen_size.x, self.screen_size.y)
        pass

    def input(self, event):
        
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if self.selection == self.start:
                self.manager.changeState(1)
            if self.selection == self.options:
                self.manager.changeState(2)
            if self.selection == self.credits:
                self.manager.changeState(3)

        if not self.outro:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.selection == self.start:
                        self.selection = self.options
                    elif self.selection == self.options:
                        self.selection = self.credits
                if event.key == pygame.K_UP:
                    if self.selection == self.options:
                        self.selection = self.start
                    elif self.selection == self.credits:
                        self.selection = self.options
                if event.key == pygame.K_k:
                    self.outro = True
                    self.intro = False
        pass

