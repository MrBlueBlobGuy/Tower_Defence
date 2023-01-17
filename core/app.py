import sys
import pygame
from .Input import Input
from .Sprite import Sprite
from .Text import Text
from .global_enable import layers

class App:
    """Runtime Class For the application"""

    Axis_dictionary = {}
    AllSprites = None
    tb = None


    def __init__(self, window_title: str, size: tuple) -> None:
        print("Thanks for trying whatever this is.\nTo report bugs go to 'https://github.com/MrBlueBlobGuy/Tower_Defence/issues'")

        self.Object = None
        self.window = None
        self.size = size
        self.FrameCount = 1
        self.window_title = window_title

        self.run()
        self.loop()

    def loop(self):
        while True:
            if self.FrameCount == 1:
                self.start()

            self.window.fill((255, 0, 255, 0))
            self.runtime()
            for layer in layers.sorting_layers:
                layers.sorting_layers[layer].update()
                layers.sorting_layers[layer].draw(self.window)
                

            pygame.display.update()
            self.FrameCount += 1
            self.check_exit()
            self.size = pygame.display.get_window_size()
            for axis in self.Axis_dictionary:
                self.Axis_dictionary[axis].set_value()

            pygame.time.Clock().tick(60)

    def run(self):
        pygame.init()
        self.window = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption(self.window_title)

    def start(self):
        """Run at the first frame before the loop starts"""
        layers.add_layer()

        self.Object = Sprite(
        color=(0, 200, 255, 0), 
        size = (20, 20), 
        position = (0, 0), 
        sprite_library_update=self.update_sprite_library,
        sorting_layer=0)

        Input(axis_name="Horizontal",
              axis_positive_key='d',
              axis_negative_key='a',
              alt_negative_key='left',
              alt_positive_key='right',
              input_library_callback=self.update_input_dictionary)

        Input(axis_name="Vertical",
              axis_positive_key="s",
              axis_negative_key="w",
              alt_negative_key='up',
              alt_positive_key='down',
              input_library_callback=self.update_input_dictionary)

        self.tb = Text("Resources/fonts/OpenDyslexic-Bold.otf", 
        self.window, 
        self.size,
        Color_Foreground=(255, 0, 0, 255),
        text="Hello")

    def runtime(self):
        """Runs every frame
        Similar to 'Update'
        Recommended not to do much complex calculations"""
        self.Object.rect.x += self.get_input("Horizontal") * 3
        self.Object.rect.y += self.get_input("Vertical") * 3
        self.tb.render_text()

    def update_sprite_library(self, sprite_object:Sprite):
        layers.add_to_layer(sprite_object.sorting_layer, sprite_object)

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
