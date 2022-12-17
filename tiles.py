import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, control):
        '''
        Инициализация тайлов
        :param pos: расположение тайла (координаты)
        :param control: строка, показывающая наличие тайлов сверху, снизу, слева и справа от данного тайла
        '''
        super().__init__()
        # Верх, Низ, Лево, Право
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
        self.rect = self.image.get_rect(topleft=pos)

    def set_tile(self, control):
        '''
        Функция устанавливает изображение тайла
        :param control: строка, показывающая наличие тайлов сверху, снизу, слева и справа от данного тайла
        '''
        path = 'graphics/tileset/'
        tile = self.tiles[control]
        full_path = path + tile
        self.image = pygame.image.load(full_path).convert_alpha()

    def update(self, x_shift):
        '''
        Функция обновления x координаты тайла
        :param x_shift: значение на которое изменяется координата x тайла
        '''
        self.rect.x += x_shift


class Objects(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        '''
        Инициализация объектов
        :param pos: расположение объекта (координаты)
        :param type: тип объекта
        '''
        super().__init__()
        self.objects = ['20.png',
                        '21.png',
                        '22.png',
                        '30.png',
                        '40.png']
        self.set_object(type)
        self.rect = self.image.get_rect(topleft=pos)

    def set_object(self, type):
        '''
        Функция устанавливает изображение объетка
        :param type: тип объекта
        '''
        path = 'graphics/tileset/'
        grass = self.objects[type]
        full_path = path + grass
        self.image = pygame.image.load(full_path).convert_alpha()

    def update(self, x_shift):
        '''
        Функция обновления x координаты объекта
        :param x_shift: значение на которое изменяется координата x объекта
        '''
        self.rect.x += x_shift
