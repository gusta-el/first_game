import pygame

class Dialog:

    def __init__(self):
        self.open = False
        self.speeches = []
        self.dialog_img = pygame.image.load("res/dialog_box.png")
        self.dialogY = -200
        self.dialogYTween = 0
        self.speech_index = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 24)
        pass

    def nextSpeech(self):
        self.speech_index += 1
        if len(self.speeches) <= self.speech_index:
            self.closeDialog()
            #Acabou as speeches

    def closeDialog(self):
        self.open = False
        self.dialogY = -200

    def openDialog(self, speeches):
        self.open = True
        self.speeches = speeches
        self.dialogY = 200
        self.speech_index = 0
        pass

    def update(self, delta):
        self.dialogYTween += (self.dialogY - self.dialogYTween)/5
        pass

    def render(self, renderer):
        renderer.drawTexture(self.dialog_img, pygame.screen_size[0]//2, pygame.screen_size[1] - self.dialogYTween)
        #Desenha o current, caso esteja aberto
        if self.open and len(self.speeches) > self.speech_index:
            renderer.drawTextWithFont(
                self.font,
                self.speeches[self.speech_index],
                pygame.screen_size[0]//2 - self.dialog_img.get_rect().width/2 + 60,
                pygame.screen_size[1] - self.dialogYTween - self.dialog_img.get_rect().height/2 + 60)
        

    def input(self, event):
        if self.open:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.nextSpeech()

        pass