from vampire_survivor.sprites import CollisionSprite
import pygame
from .settings import *
from .player import Player
from .sprites import *
from random import randint


class Game:
    def __init__(self):
        pygame.init()

        self.display_surface = pygame.display.set_mode(
            size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Suvivor")
        self.clock = pygame.time.Clock()
        self.is_running = True

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # sprites
        self.player = Player(position=(400, 300), groups=(
            self.all_sprites,), collision_sprites=self.collision_sprites)

        for _ in range(5):
            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            width, height = randint(60, 100), randint(50, 100)

            CollisionSprite(position=(x, y), size=(
                width, height), groups=(self.all_sprites, self.collision_sprites))

    def run(self):
        while self.is_running:
            dt = self.clock.tick()/1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            # update
            self.all_sprites.update(dt)

            # draw
            self.display_surface.fill("black")
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        pygame.quit()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
