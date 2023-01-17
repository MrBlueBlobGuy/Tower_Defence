import pygame


class Text:
    Black = (0, 0, 0, 255)
    White = (255, 255, 255, 255)
    Blue =  (0, 0, 255, 255)
    Green = (0, 255, 0, 255)
    Red =   (255, 0, 0, 255)

    def __init__(self, font:str, Window, Window_Size, text:str, Color_Foreground, Color_Background = (255, 255, 255, 0)) -> None:
        self.font = pygame.font.Font(font, 32)
        self.text = text
        self.text_box = self.font.render(text, True, Color_Foreground, Color_Background)
        self.tb_rect = self.text_box.get_rect()
        self.tb_rect.center = (Window_Size[0]//2, Window_Size[1]//2)
        self.window = Window

    def render_text(self):
        self.window.blit(self.text_box, self.tb_rect)