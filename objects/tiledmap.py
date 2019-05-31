import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from physics.body import Body
from objects.mapProps import MapProp

class TiledMap:

    def __init__(self, map_url):
        self.tiled_map = load_pygame(map_url)

    def render(self, renderer):
        for layer in self.tiled_map.layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    renderer.drawTexture(image, x*32, y*32, 32, 32)

    def addBodies(self, world, objectList):
        for layer in self.tiled_map.layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                for obj in layer:
                    if obj.type == "block":
                        b = Body(pygame.Vector2(obj.x - 16 + obj.width/2, obj.y - 16 + obj.height/2), 'rect', pygame.Vector2(obj.width, obj.height), 'static')
                        world.addBody(b)
                    elif obj.image != None:
                        b = MapProp(pygame.Vector2(obj.x - 16 + obj.width/2, obj.y - 16 + obj.height/2), obj.image)
                        objectList.append(b)
                        pass