import pygame

class Animation:

    def __init__(self, frames, delay):
        self.frames = frames
        self.delay = delay

    def getFrame(self, time):
        t = int(time / self.delay) % len(self.frames)
        return self.frames[t]