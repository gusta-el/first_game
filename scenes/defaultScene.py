import pygame
from pygame.math import Vector2
from scenes.scene import Scene
from scenes.character import Player
from physics.world import World
from physics.body import Body
from objects.tiledmap import TiledMap
from objects.gameobject import GameObject

class DefaultScene(Scene):

    def start(self):

        self.objects = []

        self.character1 = Player(pygame.Vector2(860, 580), self)
        self.character2 = Player(pygame.Vector2(730, 580), self)

        self.currentCharacter = self.character1

        self.objects.append(self.character1)
        self.objects.append(self.character2)
        
        self.world = World(Vector2(0, 0))

        self.tiledmap = TiledMap('res/mapas/casita.tmx')
        self.tiledmap.addBodies(self.world, self.objects)
        self.tiledmap.loadConcertos(self.objects, self)

        self.character1.control = True

        self.world.addBody(self.character1)
        self.world.addBody(self.character2)
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

    def update(self, delta):
        for obj in self.objects:
            obj.update(delta)

        self.world.update(delta)
        pass

    def sortZ(self, val):
        return val.z

    def render(self, renderer):
        self.tiledmap.render(renderer)

        self.objects.sort(key = self.sortZ)

        for obj in self.objects:
            obj.render(renderer)

        #self.world.render(renderer)
        pass