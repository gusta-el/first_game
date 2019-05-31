from abc import ABC, abstractmethod

class GameObject(ABC):

    def __init__(self):
        self.z = 0

    @abstractmethod
    def input(self, event):
        pass

    @abstractmethod
    def update(self, delta):
        pass

    @abstractmethod
    def render(self, renderer):
        pass
