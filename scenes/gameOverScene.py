import pygame
from pygame.math import Vector2
from pygame import Rect
from scenes.scene import Scene

class GameOverScene(Scene):

    def __init__(self, manager):
        super().__init__(manager)

    def start(self):
        self.game_over_song = False
        #self.mus = pygame.mixer.Sound("res/sounds/game_over.wav")
        
        self.gameOver = pygame.image.load("res/gameOver.jpg")
        self.alpha = 1
        self.screen_size = Vector2(pygame.screen_size[0], pygame.screen_size[1])
        self.zero = Vector2(self.screen_size.x/2, self.screen_size.y/2)

        rx = self.screen_size.x / 3536
        ry = self.screen_size.y / 2536

        #Botões
        self.tryAgain = Rect(-1530*rx, 445*ry, 1225*rx, 130*ry)
        self.voltarMenu = Rect(315*rx, 445*ry, 1035*rx, 130*ry)

        self.selection = self.tryAgain
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
            if self.selection == self.tryAgain:
                self.manager.changeState("Game")
            if self.selection == self.voltarMenu:
                self.manager.changeState("Menu")

        if not self.outro:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.selection == self.voltarMenu:
                        self.selection = self.tryAgain
                if event.key == pygame.K_RIGHT:
                    if self.selection == self.tryAgain:
                        self.selection = self.voltarMenu
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
                if self.selection == self.tryAgain:
                    self.manager.changeState("Game")
                    pass #Muda pra tela de jogo
                elif self.selection == self.voltarMenu:
                    self.manager.changeState("Menu")
                    pass #Muda pra tela de menu

    def render(self, renderer):
        if self.manager.sound == False:
            pygame.mixer.music.stop()
            self.menu_song  = False
        if self.manager.sound == True:        
            if self.game_over_song == False:
                #self.mus.play()
                self.result_scene_song = True


        renderer.camera_pos = Vector2(0, 0)
        renderer.drawTexture(self.gameOver, 0, 0, pygame.screen_size[0], pygame.screen_size[1])

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


