from pygame import *
from settings import *


class Menu:
    def __init__(self, font):
        self.option_surfaces = []
        self.callbacks = []
        self.current_option_index = 0
        self.font = font

    def append_option(self, option, callback):
        self.option_surfaces.append(self.font.render(option, True, (255, 255, 255)))
        self.callbacks.append(callback)

    def switch(self, direction):
        self.current_option_index = abs(len(self.option_surfaces) + self.current_option_index + direction) % len(self.option_surfaces)

    def select(self):
        self.callbacks[self.current_option_index]()

    def draw(self, surf, x, y, y_padding):
        for i in range(len(self.option_surfaces)):
            option = self.option_surfaces[i]
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * y_padding)
            if i == self.current_option_index:
                draw.rect(surf,(139, 0, 139), option_rect)
            surf.blit(option, option_rect)