import pygame
from scenes.scene import Scene
from pygame.math import Vector2
#from scenes.defaultScene import DefaultScene
import math

class ResultScene(Scene):

    def __init__(self, manager):
        super().__init__(manager)
        pass

    def start(self):


        self.result_scene_song = False

        self.alpha = 1
        self.intro = True
        self.outro = False
        self.screen_size = Vector2(pygame.screen_size[0], pygame.screen_size[1])
        self.timer = 0
        self.bg_menu_select = pygame.image.load("res/bg_menu_select.png")
        self.resultado_img = pygame.image.load("res/resultado.png")
        self.font = pygame.font.SysFont("Comic Sans MS", 24, bold=True)

        self.tween_score = 0
        self.tween_time = 0

    def update(self, delta):

        self.timer += delta

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

        if not self.intro:
            self.tween_score += (ResultScene.score - self.tween_score) / 20
            self.tween_time += (ResultScene.time - self.tween_time) / 20


    def render(self, renderer):
        if self.manager.sound == False:
            pygame.mixer.music.stop()
            self.menu_song  = False
        if self.manager.sound == True:  
            if self.result_scene_song == False:
                result_song = pygame.mixer.music.load("res/sounds/you_win.mp3")
                pygame.mixer.music.play(1)
                self.result_scene_song = True

        #Desenha fundo
        renderer.resetCamera()
        m = int(max(self.screen_size.x, self.screen_size.y))
        f = m/self.bg_menu_select.get_rect().width

        for i in range(2):
            for j in range(2):
                renderer.drawTexture(
                    self.bg_menu_select,
                    i * m + (int)(self.timer*25 % (50*f)),
                    j * self.bg_menu_select.get_rect().height * f + (int)(self.timer*25 % (50*f)),
                    scale=f
                    )

        renderer.drawTexture(self.resultado_img, 300, 100)
        renderer.setColor(255, 0, 76, 255)
        renderer.drawTextWithFont(self.font, "Tempo: " + str(int(self.tween_time)), 300, 250)
        renderer.drawTextWithFont(self.font, "Score: " + str(int(self.tween_score)), 300, 300)

        renderer.setColor(0, 0, 0, 255)
        proxima_fase = "Aperte espaço para voltar ao menu principal"
        renderer.drawTextWithFont(self.font, proxima_fase, 300, 400)

        #Desenha o fade in/out
        renderer.startShape()
        renderer.setColor(0, 0, 0, int(self.alpha * 255))
        renderer.fillRect(0, 0, self.screen_size.x, self.screen_size.y)
        renderer.endShape()


    def input(self, event):
                
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.outro = True
            self.intro = False

        pass