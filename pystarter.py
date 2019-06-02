import sys, pygame, time
from manager import Manager
from renderer import Renderer
from screeninfo import get_monitors

pygame.init()
pygame.font.init()
size = width, height = get_monitors()[0].width, get_monitors()[0].height

pygame.screen_size = size

#Game attributes
fps = 60
target = 1/fps
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
delta = 1/fps
fillColor = (0, 0, 0)
drawFps = True

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

    #Fps debug
    if drawFps:
        renderer.setColor(255, 255, 255, 255)
        renderer.drawText("FPS:" + str(int(1/delta)), 10, 10)
    pygame.display.flip()

    #Loop sleep
    end = time.time()
    elapsed = end - init
    if(target - elapsed > 0):
        time.sleep(target - elapsed)
    delta = time.time() - init