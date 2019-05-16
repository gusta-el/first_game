import pygame, math

class Renderer:
    
    def __init__(self, screen):
        self.screen = screen
        self.color = pygame.Color(255, 255, 255, 1)
        self.camera_pos = pygame.Vector2(0, 0)

    def drawLine(self, x1, y1, x2, y2):
        
        pygame.draw.line(self.screen, self.color,
        (
            x1 - self.camera_pos.x + pygame.screen_size[0]//2,
            y1 - self.camera_pos.y + pygame.screen_size[1]//2
        ),(
            x2 - self.camera_pos.x + pygame.screen_size[0]//2,
            y2 - self.camera_pos.y + pygame.screen_size[1]//2
        ))

    def drawRect(self, x, y, w, h):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(
            x - self.camera_pos.x + pygame.screen_size[0]//2,
            y - self.camera_pos.y + pygame.screen_size[1]//2,
            w, h), 1)

    def fillRect(self, x, y, w, h):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(
            x - self.camera_pos.x + pygame.screen_size[0]//2,
            y - self.camera_pos.y + pygame.screen_size[1]//2,
            w, h), 0)

    def drawCircle(self, x, y, radius):
        pygame.draw.circle(self.screen, self.color, (
            x - self.camera_pos.x + pygame.screen_size[0]//2,
            y - self.camera_pos.y + pygame.screen_size[1]//2
            ), radius, 1)

    def fillCircle(self, x, y, radius):
        pygame.draw.circle(self.screen, self.color, (
            x - self.camera_pos.x + pygame.screen_size[0]//2,
            y - self.camera_pos.y + pygame.screen_size[1]//2
            ), radius, 0)

    def setColor(self, r, g, b, a):
        self.color = pygame.Color(r, g, b, a)

    def drawTexture(self, texture, x, y, w, h, rotation=0, off_x=0, off_y=0):
        tex = pygame.transform.scale(texture, (w, h))
        tex = pygame.transform.rotate(tex, rotation)
        nx = x - math.cos(math.radians(rotation)) * off_x - math.sin(math.radians(rotation)) * off_y
        ny = y - math.cos(math.radians(rotation)) * off_y + math.sin(math.radians(rotation)) * off_x
        self.screen.blit(tex, tex.get_rect(center=(
            nx - self.camera_pos.x + pygame.screen_size[0]//2,
            ny - self.camera_pos.y + pygame.screen_size[1]//2
            )))