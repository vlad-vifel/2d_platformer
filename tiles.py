import pygame

class Tile(pygame.sprite.Sprite):

    def __init__(self, pos, size, control):
        super().__init__()
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
        # self.image = pygame.Surface((size,size))
        # self.image.fill('white')
        self.rect = self.image.get_rect(topleft = pos)

    def set_tile(self, control):
        path = 'graphics/tileset/'


        tile = self.tiles[control]
        full_path = path + tile
        self.image = pygame.image.load(full_path).convert_alpha()



    def update(self, x_shift):
        self.rect.x += x_shift
