import pygame
from pygame.sprite import Sprite as pys


class Sprite(pys):
    def __init__(self, color, size, possiton,sprite_library_update):
        super().__init__()

        self.image = pygame.Surface([size[0], size[1]])

        pygame.draw.rect(self.image,
                         rect=pygame.Rect(0, 0, size[0], size[1]),
                         color=color)

        self.rect = self.image.get_rect()

        self.rect.x = possiton[0]
        self.rect.y = possiton[1]

        sprite_library_update(self)
