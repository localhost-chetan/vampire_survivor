import pygame
from .settings import *
from pygame.sprite import Group


class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, position: tuple[float, float], size: tuple[float, float], groups: tuple[Group, ...]):
        super().__init__(*groups)
        self.image = pygame.Surface(size=size)
        self.rect = self.image.get_frect(center=position)
        self.image.fill('orange')
