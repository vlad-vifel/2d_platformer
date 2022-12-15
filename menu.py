from pygame import *

class Menu:
    def __init__(self, title_font, option_font):
        self.title_surface = None
        self.option_surfaces = []
        self.callbacks = []
        self.current_option_index = 0
        self.title_font = title_font
        self.option_font = option_font

    def append_title(self, title):
        self.title_surface = self.title_font.render(title.upper(), True, (255, 255, 255))

    def append_option(self, option, callback):
        self.option_surfaces.append(self.option_font.render(option, True, (255, 255, 255)))
        self.callbacks.append(callback)

    def switch(self, direction):
        self.current_option_index = abs(len(self.option_surfaces) + self.current_option_index + direction) % len(self.option_surfaces)

    def select(self):
        self.callbacks[self.current_option_index]()

    def draw(self, surf, x, y, y_padding):
        title = self.title_surface
        title_rect = title.get_rect()
        title_rect.topleft = (x, y)
        surf.blit(title, title_rect)
        for i in range(len(self.option_surfaces)):
            option = self.option_surfaces[i]
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + (i + 1) * y_padding + 30)
            if i == self.current_option_index:
                draw.rect(surf,(139, 0, 139), option_rect)
            surf.blit(option, option_rect)