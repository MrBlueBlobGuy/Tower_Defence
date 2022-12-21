import pygame


class Input:
    def __init__(self, axis_name: str, axis_positive_key, axis_negative_key, sprite_library_callback):
        self.axis_name = axis_name
        self.value = 0
        self.axis_positive_key = axis_positive_key
        self.axis_negative_key = axis_negative_key

        sprite_library_callback(self.axis_name, self)

    def set_value(self):
        pressed = pygame.key.get_pressed()
        if pressed[self.axis_positive_key]:
            self.value = +1.0
        elif pressed[self.axis_negative_key]:
            self.value = -1.0
        else:
            self.value = 0