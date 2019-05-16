import sys, pygame, time
from manager import Manager
from renderer import Renderer
pygame.init()
size = width, height = 640, 480

pygame.screen_size = size

#Game attributes
fps = 60
target = 1/fps
screen = pygame.display.set_mode(size)
delta = 1/fps
fillColor = (0, 0, 0)

#State Manager
manager = Manager()
manager.start()

renderer = Renderer(screen)

while 1:
    #Game Loop
    init = time.time()

    #Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        manager.input(event)    

    #Screen Render
    screen.fill(fillColor)
    manager.update(delta)
    manager.render(renderer)
    pygame.display.flip()

    #Loop sleep
    end = time.time()
    elapsed = end - init
    if(target - elapsed > 0):
        time.sleep(target - elapsed)
    delta = time.time() - init