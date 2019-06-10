import pygame
import math
from pygame.math import Vector2
from physics.body import Body
from objects.gameobject import GameObject
from objects.animation import Animation
from objects.ferramenta import Ferramenta

class Player(Body):

    def __init__(self, position, defaultScene,player):
        super().__init__(position, 'rect', Vector2(25, 14), 'dynamic')

        f = [[], [], [], []]
        if player == 1:
            self.texture = pygame.image.load("res/personagem_gordo.png")
            #63 x 128
            for j in range(4):
                for i in range(4):
                    f[j].append(self.texture.subsurface(pygame.Rect(i * 63, j * 128, 63, 128)))
        if player == 2:
            self.texture = pygame.image.load("res/personagem_magro.png")
            #63 x 128
            for j in range(4):
                for i in range(4):
                    f[j].append(self.texture.subsurface(pygame.Rect(i * 62, j * 150, 62, 150)))

        self.anim_timer = 0
        self.control = False
        self.ferramenta = None
        self.defaultScene = defaultScene

        self.acting = False

        #Images de icones de ferramentas
        self.icon_cimento = pygame.image.load("res/cimento_icon.png")
        self.icon_chave_inglesa = pygame.image.load("res/inglesa_icon.png")
        self.icon_chave_de_fenda = pygame.image.load("res/fenda_icon.png")
        self.icon_martelo = pygame.image.load("res/martelo_icon.png")
        
        self.anim_down = Animation(f[0], 1/12)
        self.anim_left = Animation(f[1], 1/12)
        self.anim_right = Animation(f[2], 1/12)
        self.anim_up = Animation(f[3], 1/12)

        self.anim_curr = self.anim_up

        self.speed = 3
        self.hor = 0
        self.ver = 0

        pass

    def render(self, renderer):
        if self.control:
            renderer.camera_pos += (self.position - renderer.camera_pos) / 10

        f = self.anim_curr.getFrame(self.anim_timer if self.velocity.length() > 1 else 0)
        renderer.drawTexture(f, self.position.x, self.position.y - 30, scale=0.6)

        if self.ferramenta != None:
            ico = None
            if self.ferramenta.type == "f_cimento":
                ico = self.icon_cimento
            elif self.ferramenta.type == "f_chave_inglesa":
                ico = self.icon_chave_inglesa
            elif self.ferramenta.type == "f_chave_de_fenda":
                ico = self.icon_chave_de_fenda
            elif self.ferramenta.type == "f_martelo":
                ico = self.icon_martelo

            if ico != None:
                renderer.drawTexture(ico, self.position.x, self.position.y - 100, scale=math.sin(self.anim_timer*3) * 0.1 + 1)

        super().render(renderer)

    def update(self, delta):
        self.anim_timer += delta
        self.z = self.position.y
        if (self.hor != 0 or self.ver != 0) and self.control:
            tvel = Vector2(self.hor, self.ver).normalize() * self.speed
        else: tvel = Vector2(0, 0)
        self.velocity += (tvel - self.velocity) / 5
        

        ang = self.velocity.angle_to(Vector2(1, 0))
        if ang < 45 and ang > -45:
            #Right: < 45 and > -45
            self.anim_curr = self.anim_right
        elif ang > 135 or ang < -135:
            #Left: > 135 or < -135
            self.anim_curr = self.anim_left
        elif ang < 135 and ang > 45:
            #Up: < 135 and > 45
            self.anim_curr = self.anim_up
        elif ang < -45 or ang > -135:
            #Down: < -45 and > -135
            self.anim_curr = self.anim_down

    def input(self, event):
        if(self.control):

            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_z:
                    self.acting = True

                if event.key == pygame.K_x:
                    if self.ferramenta != None:
                        
                        self.ferramenta.x = self.position.x
                        self.ferramenta.y = self.position.y
                        f = Ferramenta(self.ferramenta, self.defaultScene)
                        self.defaultScene.objects.append(f)
                        self.ferramenta = None

                if event.key == pygame.K_LEFT:
                    self.hor = -1
                elif event.key == pygame.K_RIGHT:
                    self.hor = 1
                elif event.key == pygame.K_UP:
                    self.ver = -1
                elif event.key == pygame.K_DOWN:
                    self.ver = 1

            if event.type == pygame.KEYUP:
                if event.key ==  pygame.K_z:
                    self.acting = False

                if event.key == pygame.K_LEFT:
                    if pygame.key.get_pressed()[pygame.K_RIGHT]:
                        self.hor = 1
                    else:
                        self.hor = 0
                elif event.key == pygame.K_RIGHT:
                    if pygame.key.get_pressed()[pygame.K_LEFT]:
                        self.hor = -1
                    else:
                        self.hor = 0
                elif event.key == pygame.K_UP:
                    if pygame.key.get_pressed()[pygame.K_DOWN]:
                        self.ver = 1
                    else:
                        self.ver = 0
                elif event.key == pygame.K_DOWN:
                    if pygame.key.get_pressed()[pygame.K_UP]:
                        self.ver = 1
                    else:
                        self.ver = 0
        pass
