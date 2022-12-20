import pygame
from pygame.sprite import Sprite as pys


class Sprite(pys):
    def __init__(self, color, height, width, sprite_library_update):
        super().__init__()

        self.image = pygame.Surface([width, height])

        pygame.draw.rect(self.image,
                         rect=pygame.Rect(0, 0, width, height),
                         color=color)

        self.rect = self.image.get_rect()

        sprite_library_update(self)
