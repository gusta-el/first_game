import pygame, math
from pygame.math import Vector2

class Renderer:
    
    def __init__(self, screen):
        self.screen = screen
        self.color = pygame.Color(255, 255, 255, 1)
        self.camera_pos = Vector2(0, 0)
        self.font = pygame.font.SysFont('Comic Sans MS', 15)
        self.shape_surface = pygame.Surface(pygame.screen_size, pygame.SRCALPHA)

    def produceSound(self,sound):
        crash_sound = pygame.mixer.Sound("res/sounds/" + sound + ".wav")
        pygame.mixer.Sound.play(crash_sound)

    def drawText(self, text, x, y, color=None):
        if color == None:
            s = self.font.render(text, False, self.color)
        else:
            s = self.font.render(text, False, color)
        s.set_alpha(self.color.a)
        self.screen.blit(s, (x, y))

    def drawScoreAndTime(self, text, x, y):
        self.color = pygame.Color(255, 255, 255, 1)
        self.font = pygame.font.SysFont('Comic Sans MS', 15)
        s.set_alpha(self.color.a)
        self.screen.blit(s, (x, y))

    #World to screen
    def project(self, position):
        return Vector2(
                position.x - self.camera_pos.x + pygame.screen_size[0]//2,
                position.y - self.camera_pos.y + pygame.screen_size[1]//2
                )

    #Screen to World
    def unproject(self, position):
        return Vector2(
                position.x + self.camera_pos.x - pygame.screen_size[0]//2,
                position.y + self.camera_pos.y - pygame.screen_size[1]//2
                )

    def startShape(self):
        self.shape_surface.fill(pygame.Color(0, 0, 0, 0))

    def endShape(self):
        self.screen.blit(self.shape_surface, (0, 0))

    def drawLine(self, x1, y1, x2, y2):
        #self.shape_surface.set_alpha(self.color.a)
        pygame.draw.line(self.shape_surface, self.color,
        (
            x1 - self.camera_pos.x + pygame.screen_size[0]//2,
            y1 - self.camera_pos.y + pygame.screen_size[1]//2
        ),(
            x2 - self.camera_pos.x + pygame.screen_size[0]//2,
            y2 - self.camera_pos.y + pygame.screen_size[1]//2
        ))

    def drawRect(self, x, y, w, h):
        #self.shape_surface.set_alpha(self.color.a)
        pygame.draw.rect(self.shape_surface, self.color, pygame.Rect(
            x - self.camera_pos.x + pygame.screen_size[0]//2,
            y - self.camera_pos.y + pygame.screen_size[1]//2,
            w, h), 2)

    def fillRect(self, x, y, w, h):
        #self.shape_surface.set_alpha(self.color.a)
        pygame.draw.rect(self.shape_surface, self.color, pygame.Rect(
            x - self.camera_pos.x + pygame.screen_size[0]//2,
            y - self.camera_pos.y + pygame.screen_size[1]//2,
            w, h), 0)

    def drawCircle(self, x, y, radius):
        #self.shape_surface.set_alpha(self.color.a)
        pygame.draw.circle(self.shape_surface, self.color, (
            x - self.camera_pos.x + pygame.screen_size[0]//2,
            y - self.camera_pos.y + pygame.screen_size[1]//2
            ), radius, 1)

    def fillCircle(self, x, y, radius):
        #self.shape_surface.set_alpha(self.color.a)
        pygame.draw.circle(self.shape_surface, self.color, (
            int(x - self.camera_pos.x + pygame.screen_size[0]//2),
            int(y - self.camera_pos.y + pygame.screen_size[1]//2)
            ), radius, 0)

    def setColor(self, r, g, b, a):
        self.color = pygame.Color(r, g, b, a)

    def drawTexture(self, texture, x, y, w=None, h=None, rotation=0, off_x=0, off_y=0, scale=1):
        if w == None: w = int(texture.get_rect().width * scale)
        if h == None: h = int(texture.get_rect().height * scale)
        tex = pygame.transform.scale(texture, (w, h))
        tex = pygame.transform.rotate(tex, rotation)
        nx = x - math.cos(math.radians(rotation)) * off_x - math.sin(math.radians(rotation)) * off_y
        ny = y - math.cos(math.radians(rotation)) * off_y + math.sin(math.radians(rotation)) * off_x
        self.screen.blit(tex, tex.get_rect(center=(
            nx - self.camera_pos.x + pygame.screen_size[0]//2,
            ny - self.camera_pos.y + pygame.screen_size[1]//2
            )))