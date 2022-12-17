from os import walk
import pygame

'''Заимствование кода, код взят с https://github.com/clear-code-projects/2D-Mario-style-platformer'''
def import_folder(path):
    '''
    Функция конвертации папки изображений в список путей до изображений папки
    :param path: путь до папки
    :return: список путей до изображений папки
    '''
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:

            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
'''Конец заимствования кода'''