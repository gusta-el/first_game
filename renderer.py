import pygame

class Renderer:

    def __init__(self, screen):
        self.screen = screen
        pass

    def drawLine(self, x1, y1, x2, y2):
        pass

    def drawRect(self, x, y, w, h):
        pass

    def drawCircle(self, x, y, radius):
        pass

    def setColor(self, color):
        pass

    def drawTexture(self, texture, x, y, w, h):
        tex = texture
        tex = pygame.transform.scale(tex, (w, h))
        self.screen.blit(tex, pygame.Rect(x, y, 0, 0))
        pass

    def drawTexture(self, texture, x, y, w, h, rotation):
        tex = texture
        tex = pygame.transform.rotozoom(tex, rotation, 1)
        tex = pygame.transform.scale(tex, (w, h))
        self.screen.blit(tex, pygame.Rect(x, y, 0, 0))
        pass