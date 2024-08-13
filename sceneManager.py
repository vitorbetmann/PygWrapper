import sys
import time

import pygame


class SceneManager:
    def __init__(self, screen, scenes: dict):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.scenes = scenes
        for scene in self.scenes.values():
            scene.scene_manager = self
        self.current_scene = self.scenes.get("start")
        self.current_scene.enter()

        self._dt, self._prev_time = 0, 0

        # self.clock = pygame.time.Clock()  # Uncomment if FPS capping desired.

    def add_scene(self, scene: dict):
        self.scenes.update(scene)

    def remove_scene(self, scene_name: str):
        self.scenes.pop(scene_name, None)

    def goto(self, next_scene_name: str):
        scene_data = self.current_scene.leave()
        self.current_scene = self.scenes.get(next_scene_name)
        self.current_scene.enter(scene_data)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.current_scene.handle_event(event)
            self.current_scene.update(self.dt)
            self.current_scene.draw()
            pygame.display.update()
            # self.clock.tick(FPS)  # Uncomment if FPS capping is desired.

    @property
    def dt(self):
        now = time.time()
        self._dt = now - self.prev_time
        self._prev_time = now
        return self._dt

    @property
    def prev_time(self):
        return self._prev_time
