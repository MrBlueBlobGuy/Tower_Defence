import sys
import pygame
from .Sprite import Sprite


class App:
    def __init__(self, size: tuple):
        self.window = None
        self.size = size

        self.run()
        self.loop()
        self.AllSprites = pygame.sprite.Group()

    def loop(self):
        while True:
            self.check_exit()
            self.window.fill((0, 255, 255, 100))
            self.runtime()
            pygame.display.update()
            self.AllSprites.update()
            self.AllSprites.draw(self.window)
            pygame.time.Clock().tick(60)

    def run(self):
        pygame.init()
        self.window = pygame.display.set_mode(self.size)

    @staticmethod
    def check_exit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def runtime(self):
        """Runs every frame
        Similar to 'Update'
        Recommended to not do much complex calculations"""
        pass

    def update_sprite_library(self, sprite_object: Sprite):
        pass