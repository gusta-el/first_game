import pygame, time
from pygame.math import Vector2
from scenes.scene import Scene
from scenes.character import Player
from physics.world import World
from physics.body import Body
from objects.tiledmap import TiledMap
from objects.gameobject import GameObject
from objects.particle import Particle
from datetime import datetime
import random
from scenes.resultScene import ResultScene

class DefaultScene(Scene):

    mapa = "batata"

    def start(self):

        self.intro = True
        self.outro = False
        self.alpha = 1
        self.screen_size = Vector2(pygame.screen_size[0], pygame.screen_size[1])

        self.transition_end = False
        self.deadline_time = 60
        self.initial_time  = 0

        self.complete_img = pygame.image.load("res/complete.png")
        self.complete_y = -300
        self.complete_rot = 0
        
        self.objects = []
        self.character1 = Player(Vector2(860, 580), self,1)
        self.character2 = Player(Vector2(730, 580), self,2)

        self.currentCharacter = self.character1
        self.objects.append(self.character1)
        self.objects.append(self.character2)

        self.particles = []
        
        self.world = World(Vector2(0, 0))

        self.tiledmap = TiledMap(DefaultScene.mapa)
        self.tiledmap.addBodies(self.world, self.objects)
        self.total_concertos = 0
        self.tiledmap.loadConcertos(self.objects, self)

        self.world.addBody(self.character1)
        self.world.addBody(self.character2)
        
        self.character1.control = True

        self.score = 0
        pass

    def completeLevel(self):
        self.transition_end = True
        self.character1.control = False
        self.character2.control = False
        pass

    def input(self, event):
        for obj in self.objects:
            obj.input(event)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.character1.control == True:
                    self.character1.control = False
                    self.character2.control = True
                    self.currentCharacter = self.character2
                else:
                    self.character1.control = True
                    self.character2.control = False    
                    self.currentCharacter = self.character1
        pass

    def removeObject(self, object):
        self.objects.remove(object)

    def addParticle(self, position, cor):
        vel = Vector2(random.random() * 2 - 1, random.random() * 2 - 1).normalize() * 1
        p = Particle(position, vel, Vector2(0, 0), random.randrange(3, 5), cor, self)
        self.objects.append(p)

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
                if self.transition_end:
                    ResultScene.time = self.deadline_time - self.initial_time
                    ResultScene.score = self.score
                    self.manager.changeState("Result")
                else:
                    self.manager.changeState("GameOver")

                #Terminou a outro 
        
        for obj in self.objects:
            obj.update(delta)

        self.world.update(delta)

        if not self.transition_end:
            self.initial_time += delta

        if self.initial_time >= self.deadline_time:
            self.intro = False
            self.outro = True

        if self.transition_end:
            if self.complete_y < 300:
                self.complete_y += delta * 300
            else:
                if self.complete_rot < 360:
                    self.complete_rot += delta * 300
                else:
                    self.outro = True

    def sortZ(self, val):
        return val.z

    def render(self, renderer):
        self.tiledmap.render(renderer)

        self.objects.sort(key = self.sortZ)

        renderer.startShape()
        for obj in self.objects:
            obj.render(renderer)
        renderer.endShape()
        #self.world.render(renderer)
        renderer.setColor(255, 255, 255, 255)

        renderer.drawText("PONTUAÇÃO", 70, 10)
        renderer.drawText(str(self.score) , 110, 25)
        
        renderer.drawText("TEMPO", 320, 10)
        if self.deadline_time - self.initial_time < 5:
            renderer.drawText(str(int(self.deadline_time - self.initial_time)), 340, 25, pygame.Color(255, 0, 0, 1))
        else: 
            renderer.drawText(str(int(self.deadline_time - self.initial_time)), 340, 25)
        pass

        lastPos = Vector2(renderer.camera_pos.x, renderer.camera_pos.y)

        renderer.resetCamera()
        renderer.drawTexture(self.complete_img, pygame.screen_size[0]//2, self.complete_y, rotation=self.complete_rot)
        
        #Desenha o fade in/out
        renderer.startShape()
        renderer.setColor(0, 0, 0, int(self.alpha * 255))
        renderer.fillRect(0, 0, self.screen_size.x, self.screen_size.y)
        renderer.endShape()
        
        renderer.camera_pos = lastPos