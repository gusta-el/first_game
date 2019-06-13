import pygame
import pytmx
from pygame.math import Vector2
from pytmx.util_pygame import load_pygame
from physics.body import Body
from objects.mapProps import MapProp
from objects.concerto import Concerto
from objects.ferramenta import Ferramenta

class TiledMap:

    def __init__(self, map_url):
        self.tiled_map = load_pygame(map_url)

    def loadConcertos(self, objectList, defaultScene):
        for layer in self.tiled_map.layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                for obj in layer:
                    if obj.image != None and obj.type != None:
                        if obj.type[:2] == "c_":
                            c = Concerto(obj, defaultScene)
                            objectList.append(c)
                            defaultScene.total_concertos += 1
                        if obj.type[:2] == "f_":
                            f = Ferramenta(obj, defaultScene)
                            objectList.append(f)



    def render(self, renderer):
        for layer in self.tiled_map.layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    #Checa se de fato o tile ta na tela
                    proj = renderer.project(Vector2(x*32, y*32))
                    if(proj.x >= -16 and proj.x <= pygame.screen_size[0] + 16):
                        if(proj.y >= -16 and proj.y <= pygame.screen_size[1] + 16):
                            renderer.drawTexture(image, x*32, y*32, 32, 32)

    def addBodies(self, world, objectList):
        for layer in self.tiled_map.layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                for obj in layer:
                    if obj.type == "block":
                        b = Body(Vector2(obj.x - 16 + obj.width/2, obj.y - 16 + obj.height/2), 'rect', Vector2(obj.width, obj.height), 'static')
                        world.addBody(b)
                    if obj.image != None and obj.type == "block" or obj.type == "":
                        b = MapProp(Vector2(obj.x - 16 + obj.width/2, obj.y - 16 + obj.height/2), obj.image)
                        objectList.append(b)
                        pass