from abc import ABC, abstractmethod

class Scene(ABC):

    def __init__(self, manager):
        self.manager = manager

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def input(self, keys):
        pass

    @abstractmethod
    def update(self, delta):
        pass

    @abstractmethod
    def render(self, renderer):
        pass
