import pygame
from scenes.scene import Scene
from pygame.math import Vector2
from scenes.defaultScene import DefaultScene
import math

class LevelSelectScene(Scene):

    def __init__(self, manager):
        super().__init__(manager)
        pass

    def start(self):
        self.alpha = 1
        self.intro = True
        self.outro = False
        self.screen_size = Vector2(pygame.screen_size[0], pygame.screen_size[1])

        self.fases_icon = [
            pygame.image.load("res/tuto_icon.png"),
            pygame.image.load("res/fase1_icon.png")
        ]
        self.open_levels = [
            True,
            False
        ]
        self.map_urls = [
            "res/mapas/casita.tmx",
            "nada"
        ]
        self.cadeado = pygame.image.load("res/cadeado.png")

        self.icon_selection = pygame.image.load("res/icon_selection.png")

        self.timer = 0

        self.selection = 0
        self.selectionTween = 0

        self.bg_menu_select = pygame.image.load("res/bg_menu_select.png")

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
                #Terminou a outro
                #Checa qual a fase, carrega ela no mapa, e troca de cena
                DefaultScene.mapa = self.map_urls[self.selection // 400]
                self.manager.changeState("Game")


        self.selectionTween += (self.selection - self.selectionTween) / 7
        pass

    def render(self, renderer):

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

        #Desenha levels
        renderer.drawTexture(self.icon_selection, self.screen_size.x//2, self.screen_size.y//2 - 200, scale=(2 + (math.sin(self.timer * 10) * 2 - 1) * 0.1))
        for i in range(len(self.fases_icon)):
            texTinted = self.fases_icon[i].copy()
            if not self.open_levels[i]:
                texTinted.fill((0, 0, 0, 255), special_flags=pygame.BLEND_MULT)
                renderer.drawTexture(self.cadeado, i * 400 + self.screen_size.x//2 - self.selectionTween, self.screen_size.y//2, scale=2)

            renderer.drawTexture(texTinted, i * 400 + self.screen_size.x//2 - self.selectionTween, self.screen_size.y//2, scale=2)

        #Desenha o fade in/out
        renderer.startShape()
        renderer.setColor(0, 0, 0, int(self.alpha * 255))
        renderer.fillRect(0, 0, self.screen_size.x, self.screen_size.y)
        renderer.endShape()
        pass

    def input(self, event):

    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if self.selection > 0:
                    self.selection -= 400
            if event.key == pygame.K_RIGHT:
                if self.selection < (len(self.fases_icon)-1) * 400:
                    self.selection += 400

            if event.key == pygame.K_SPACE:
                if self.open_levels[self.selection // 400]:
                    self.intro = False
                    self.outro = True

        pass