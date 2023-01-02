import pygame
import os
from dotenv import load_dotenv
import logging

load_dotenv()


class Input:
    KEYS = {
        'a': pygame.K_a,
        'b': pygame.K_b,
        'c': pygame.K_c,
        'd': pygame.K_d,
        'e': pygame.K_e,
        'f': pygame.K_f,
        'g': pygame.K_g,
        'h': pygame.K_h,
        'i': pygame.K_i,
        'j': pygame.K_j,
        'k': pygame.K_k,
        'l': pygame.K_l,
        'm': pygame.K_m,
        'n': pygame.K_n,
        'o': pygame.K_o,
        'p': pygame.K_p,
        'q': pygame.K_q,
        'r': pygame.K_r,
        's': pygame.K_s,
        't': pygame.K_t,
        'u': pygame.K_u,
        'v': pygame.K_v,
        'w': pygame.K_w,
        'x': pygame.K_x,
        'y': pygame.K_y,
        'z': pygame.K_z,
        'end': pygame.K_END,
        'up': pygame.K_UP,
        'down': pygame.K_DOWN,
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT
    }
    root_input_axes_folder = os.getenv('AXES_ROOT')
    input_axes_files_names = os.listdir(root_input_axes_folder)
    input_axes_files_paths = []

    def __init__(self,
                 axis_name: str,
                 axis_positive_key,
                 axis_negative_key,
                 input_library_callback,
                 alt_positive_key=None,
                 alt_negative_key=None):
        self.axis_name = axis_name
        self.value = 0
        try:
            self.axis_positive_key = self.KEYS[axis_positive_key]
            self.axis_negative_key = self.KEYS[axis_negative_key]
            self.alt_positive_key = self.KEYS[alt_positive_key] if alt_positive_key is not None else self.KEYS['end']
            self.alt_negative_key = self.KEYS[alt_negative_key] if alt_negative_key is not None else self.KEYS['end']
        except KeyError as error:
            print(f'error occurred while mapping input axis {axis_name}: {error}')
            self.axis_positive_key = None
            self.axis_negative_key = None
            self.alt_positive_key = None
            self.alt_negative_key = None

        for i in self.input_axes_files_names:
            i = f'{self.root_input_axes_folder}{i}'
            self.input_axes_files_paths.append(i)

        input_library_callback(self.axis_name, self)

    def set_value(self):
        pressed = pygame.key.get_pressed()
        if (self.axis_negative_key or self.axis_positive_key) is None:
            return
        if pressed[self.axis_positive_key] or pressed[self.alt_positive_key]:
            self.value = +1.0
        elif pressed[self.axis_negative_key] or pressed[self.alt_negative_key]:
            self.value = -1.0
        else:
            self.value = 0

    @staticmethod
    def get_input_files(callback):
        pass
