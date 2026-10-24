import pygame
from os.path import abspath, join, dirname


ASSET_DIR = abspath(join(
    dirname(__file__), "..", "assets"))


def get_asset_path(*parts: str) -> str:
    return join(ASSET_DIR, *parts)


class Player(pygame.sprite.Sprite):
    def __init__(self, position: tuple, groups: tuple):
        super().__init__(*groups)
        self.image = pygame.image.load(
            get_asset_path("images", "player", "down", "0.png"))
        self.rect = self.image.get_frect(center=position)

        # movement
        self.direction = pygame.Vector2()
        self.speed = 500

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt: float):
        self.rect.center += ((self.direction*self.speed) * dt)

    def update(self, dt: float):
        self.input()
        self.move(dt)
