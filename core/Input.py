import pygame
import os
from dotenv import load_dotenv

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
        'z': pygame.K_z
    }
    root_input_axes_folder = os.getenv('AXES_ROOT')
    input_axes_files_names = os.listdir(root_input_axes_folder)
    input_axes_files_paths = []

    def __init__(self, axis_name: str, axis_positive_key, axis_negative_key, input_library_callback):
        self.axis_name = axis_name
        self.value = 0
        self.axis_positive_key = self.KEYS[axis_positive_key]
        self.axis_negative_key = self.KEYS[axis_negative_key]

        for i in self.input_axes_files_names:
            i = f'{self.root_input_axes_folder}{i}'
            self.input_axes_files_paths.append(i)

        input_library_callback(self.axis_name, self)

    def set_value(self):
        pressed = pygame.key.get_pressed()
        if pressed[self.axis_positive_key]:
            self.value = +1.0
        elif pressed[self.axis_negative_key]:
            self.value = -1.0
        else:
            self.value = 0

    @staticmethod
    def get_input_files(callback):
        pass
