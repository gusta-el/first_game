import pygame, math

class Renderer:
    
    def __init__(self, screen):
        self.screen = screen
        self.color = pygame.Color(255, 255, 255, 1)
        self.camera_pos = pygame.Vector2(0, 0)
        self.font = pygame.font.SysFont('Comic Sans MS', 15)

    def drawText(self, text, x, y):
        s = self.font.render(text, False, self.color)
        s.set_alpha(self.color.a)
        self.screen.blit(s, (x, y))

    #World to screen
    def project(self, position):
        return pygame.Vector2(
                position.x - self.camera_pos.x + pygame.screen_size[0]//2,
                position.y - self.camera_pos.y + pygame.screen_size[1]//2
                )

    #Screen to World
    def unproject(self, position):
        return pygame.Vector2(
                position.x + self.camera_pos.x - pygame.screen_size[0]//2,
                position.y + self.camera_pos.y - pygame.screen_size[1]//2
                )


    def drawLine(self, x1, y1, x2, y2):
        s = pygame.Surface(pygame.screen_size, pygame.SRCALPHA)
        s.set_alpha(self.color.a)
        pygame.draw.line(s, self.color,
        (
            x1 - self.camera_pos.x + pygame.screen_size[0]//2,
            y1 - self.camera_pos.y + pygame.screen_size[1]//2
        ),(
            x2 - self.camera_pos.x + pygame.screen_size[0]//2,
            y2 - self.camera_pos.y + pygame.screen_size[1]//2
        ))
        self.screen.blit(s, (0, 0))

    def drawRect(self, x, y, w, h):
        s = pygame.Surface(pygame.screen_size, pygame.SRCALPHA)
        s.set_alpha(self.color.a)
        pygame.draw.rect(s, self.color, pygame.Rect(
            x - self.camera_pos.x + pygame.screen_size[0]//2,
            y - self.camera_pos.y + pygame.screen_size[1]//2,
            w, h), 2)
        self.screen.blit(s, (0, 0))

    def fillRect(self, x, y, w, h):
        s = pygame.Surface(pygame.screen_size, pygame.SRCALPHA)
        s.set_alpha(self.color.a)
        pygame.draw.rect(s, self.color, pygame.Rect(
            x - self.camera_pos.x + pygame.screen_size[0]//2,
            y - self.camera_pos.y + pygame.screen_size[1]//2,
            w, h), 0)
        self.screen.blit(s, (0, 0))

    def drawCircle(self, x, y, radius):
        s = pygame.Surface(pygame.screen_size, pygame.SRCALPHA)
        s.set_alpha(self.color.a)
        pygame.draw.circle(s, self.color, (
            x - self.camera_pos.x + pygame.screen_size[0]//2,
            y - self.camera_pos.y + pygame.screen_size[1]//2
            ), radius, 1)
        self.screen.blit(s, (0, 0))

    def fillCircle(self, x, y, radius):
        s = pygame.Surface(pygame.screen_size, pygame.SRCALPHA)
        s.set_alpha(self.color.a)
        pygame.draw.circle(s, self.color, (
            x - self.camera_pos.x + pygame.screen_size[0]//2,
            y - self.camera_pos.y + pygame.screen_size[1]//2
            ), radius, 0)
        self.screen.blit(s, (0, 0))

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