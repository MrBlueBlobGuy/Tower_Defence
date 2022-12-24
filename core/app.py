import sys
import pygame
from .Input import Input
from .Sprite import Sprite


class App:
    """Runtime Class For the application"""

    Axis_dictionary = {}
    AllSprites = None

    def __init__(self, window_title: str, size: tuple) -> None:
        self.Object = None
        self.window = None
        self.size = size
        self.AllSprites = pygame.sprite.Group()
        self.FrameCount = 1
        self.window_title = window_title

        self.run()
        self.loop()

    def loop(self):
        while True:
            if self.FrameCount == 1:
                self.start()

            self.window.fill((0, 255, 255, 100))
            self.runtime()
            self.AllSprites.update()
            self.AllSprites.draw(self.window)
            pygame.display.update()
            self.FrameCount += 1
            self.check_exit()
            self.size = pygame.display.get_window_size()
            pygame.time.Clock().tick(60)

            for axis in self.Axis_dictionary:
                self.Axis_dictionary[axis].set_value()

    def run(self):
        pygame.init()
        self.window = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption(self.window_title)

    def start(self):
        """Run at the first frame before the loop starts"""
        self.Object = Sprite((255, 0, 0, 0), (20, 20), (0, 0), self.update_sprite_library)

        Input(axis_name="Horizontal",
              axis_positive_key='d',
              axis_negative_key='a',
              input_library_callback=self.update_input_dictionary)

        Input(axis_name="Vertical",
              axis_positive_key="s",
              axis_negative_key="w",
              input_library_callback=self.update_input_dictionary)

    def runtime(self):
        """Runs every frame
        Similar to 'Update'
        Recommended not to do much complex calculations"""
        self.Object.rect.x += self.get_input("Horizontal") * 1.5
        self.Object.rect.y += self.get_input("Vertical") * 1.5

    def update_sprite_library(self, sprite_object: Sprite):
        self.AllSprites.add(sprite_object)

    def update_input_dictionary(self, axis_name: str, value: Input):
        self.Axis_dictionary[axis_name] = value

    def get_input(self, axis: str):
        """Takes in axis and returns the axis value for that axis in that frame"""
        try:
            return self.Axis_dictionary[axis].value
        except KeyError as err:
            print(f"{err}")
            return

    @staticmethod
    def check_exit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
