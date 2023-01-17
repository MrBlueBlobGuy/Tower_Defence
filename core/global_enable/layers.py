import pygame

sorting_layers = {}

def add_layer():
    """Adds a sorting layer. When making layers make sure to add layers in the order of rendering"""
    sorting_layers[len(sorting_layers)] = pygame.sprite.Group()

def add_to_layer(layer, obj):
    try:
        sorting_layers[layer].add(obj)
    except KeyError:
        return
