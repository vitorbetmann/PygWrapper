from abc import ABC, abstractmethod


class Scene(ABC):
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.scene_manager = None

    @abstractmethod
    def reset(self):
        raise NotImplementedError

    @abstractmethod
    def enter(self):
        raise NotImplementedError

    @abstractmethod
    def leave(self):
        raise NotImplementedError

    @abstractmethod
    def handle_event(self, event):
        raise NotImplementedError

    @abstractmethod
    def update(self, dt):
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        raise NotImplementedError
