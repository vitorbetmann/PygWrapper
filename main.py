import pygame

from constants import *
from sceneManager import SceneManager

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

scenes = {}

sm = SceneManager(screen, scenes)
sm.run()
