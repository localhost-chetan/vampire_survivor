import pygame
from .settings import *
from .player import Player


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

        self.player = Player(position=(400, 300), groups=(self.all_sprites,))

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
