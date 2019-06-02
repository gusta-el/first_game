import pygame
from pygame.math import Vector2
from physics.body import Body
from objects.gameobject import GameObject
from objects.animation import Animation

class Player(Body):

    def __init__(self, position):
        super().__init__(position, 'rect', pygame.Vector2(25, 14), 'dynamic')
        self.texture = pygame.image.load("res/personagem_gordo.png")
        self.anim_timer = 0
        self.control = False

        #63 x 128

        f = [[], [], [], []]

        for j in range(4):
            for i in range(4):
                f[j].append(self.texture.subsurface(pygame.Rect(i * 63, j * 128, 63, 128)))

        
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
            renderer.camera_pos += (self.position - renderer.camera_pos) / 5

        f = self.anim_curr.getFrame(self.anim_timer if self.velocity.length() > 1 else 0)
        renderer.drawTexture(f, self.position.x, self.position.y - 30, scale=0.6)
        super().render(renderer)

    def update(self, delta):
        self.anim_timer += delta
        self.z = self.position.y
        if (self.hor != 0 or self.ver != 0) and self.control:
            tvel = Vector2(self.hor, self.ver).normalize() * self.speed
        else: tvel = Vector2(0, 0)
        self.velocity += (tvel - self.velocity) / 5

        ang = self.velocity.angle_to(pygame.Vector2(1, 0))
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

        print()

    def input(self, event):
        if(self.control):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.hor = -1
                elif event.key == pygame.K_RIGHT:
                    self.hor = 1
                elif event.key == pygame.K_UP:
                    self.ver = -1
                elif event.key == pygame.K_DOWN:
                    self.ver = 1

            if event.type == pygame.KEYUP:
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

