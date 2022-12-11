import pygame
from support import import_folder

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, control):
        super().__init__()
        # UDLR (Up Down Left Right positions)
        self.tiles = {
            '0001': '00.png',
            '0000': '01.png',
            '0011': '01.png',
            '0010': '02.png',
            '0101': '10.png',
            '0111': '11.png',
            '0100': '11.png',
            '0110': '12.png',
            '1101': '13.png',
            '1111': '14.png',
            '1100': '14.png',
            '1110': '15.png',
            '1001': '16.png',
            '1011': '17.png',
            '1000': '17.png',
            '1010': '18.png',
        }
        self.set_tile(control)
        self.rect = self.image.get_rect(topleft = pos)

    def set_tile(self, control):
        path = 'graphics/tileset/'
        tile = self.tiles[control]
        full_path = path + tile
        self.image = pygame.image.load(full_path).convert_alpha()

    def update(self, x_shift):
        self.rect.x += x_shift
class Grass(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        self.grasses = ['20.png',
                        '21.png',
                        '22.png',
                        '23.png']
        self.set_grass(type)
        self.rect = self.image.get_rect(topleft = pos)

    def set_grass(self, type):
        path = 'graphics/tileset/'
        grass = self.grasses[type]
        full_path = path + grass
        self.image = pygame.image.load(full_path).convert_alpha()

    def update(self, x_shift):
        self.rect.x += x_shift

class Tile1(pygame.sprite.Sprite):
    def __init__(self,size,x,y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self,shift):
        self.rect.x += shift
class AnimatedTile(Tile1):
    def __init__(self, size, x, y, path):
        super().__init__(size, x, y)
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, shift):
        self.animate()
        self.rect.x += shift