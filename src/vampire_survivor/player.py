import pygame
from os.path import abspath, join, dirname
from pygame.sprite import Group
from typing import Literal


ASSET_DIR = abspath(join(
    dirname(__file__), "..", "assets"))


def get_asset_path(*parts: str) -> str:
    return join(ASSET_DIR, *parts)


class Player(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], groups: tuple[Group, ...], collision_sprites: Group):
        super().__init__(*groups)
        self.image = pygame.image.load(
            get_asset_path("images", "player", "down", "0.png"))
        self.rect = self.image.get_frect(center=position)
        self.hitbox_rect = self.rect.inflate(-60, -10)

        # movement
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def collision(self, axis: Literal["horizontal", "vertical"]):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if axis == "horizontal":
                    if self.direction.x > 0:
                        self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.direction.y < 0:
                        self.hitbox_rect.top = sprite.rect.bottom
                    if self.direction.y > 0:
                        self.hitbox_rect.bottom = sprite.rect.top

    def move(self, dt: float):
        self.hitbox_rect.x += ((self.direction.x * self.speed) * dt)
        self.collision("horizontal")
        self.hitbox_rect.y += ((self.direction.y * self.speed) * dt)
        self.collision("vertical")
        # Keep the rendered sprite aligned with the hitbox after movement/collision.
        self.rect.center = self.hitbox_rect.center

    def update(self, dt: float):
        self.input()
        self.move(dt)
