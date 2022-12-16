import pygame, sys
from settings import *
from level import Level
from menu import Menu

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

ARIAL_50 = pygame.font.SysFont('arial', 50)
ARIAL_70 = pygame.font.SysFont('arial', 70)

pygame.mixer.init()
pygame.mixer.music.load("music/main.mp3")
pygame.mixer.music.set_volume(0.10)
pygame.mixer.music.play(-1)

current_level = 0


def switch_scene(scene):
    '''
    Функция смены отображаемого на экране
    :param scene:
    :return:
    '''
    global current_scene
    current_scene = scene


def game_menu(menu):
    '''
    Функция создания меню
    :param menu: класс Меню
    '''
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    menu.switch(-1)
                if event.key == pygame.K_DOWN:
                    menu.switch(1)
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    switch_scene(menu.select())
        screen.fill(pygame.color.THECOLORS['black'])
        menu.draw(screen, 200, 150, 100)
        pygame.display.update()


def change_music_volume(vol):
    '''
    Функция изменения громкости звука
    :param vol: значения на которое изменяется звук за нажатие
    '''
    volume = pygame.mixer.music.get_volume() + vol
    if 0 <= volume <= 1:
        pygame.mixer.music.unpause()
        pygame.mixer.music.set_volume(volume)
    elif volume < 0:
        pygame.mixer.music.pause()
        pygame.mixer.music.set_volume(0)


def game(level_map, lives=3, current_checkpoint=0):
    '''
    Функция игры, открытие нужного уровня
    :param level_map: нужный левел
    :param lives: количество жизней
    :param current_checkpoint: место спауна
    '''
    level = Level(level_map, screen, ARIAL_50, lives, current_checkpoint)
    global current_level
    current_level = level_maps.index(level_map)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    switch_scene(game_menu(main_menu))

        if level.is_falling_death:
            switch_scene(game(level_map, lives - 1, level.current_checkpoint))

        if level.is_finished:
            if current_level + 1 == len(level_maps):
                switch_scene(game_menu(congratulations_message))
            else:
                switch_scene(game_menu(next_level_message))

        if level.gameover:
            switch_scene(game_menu(gameover_message))

        screen.fill(pygame.color.THECOLORS['lightblue1'])
        level.run()
        pygame.display.update()
        clock.tick(60)


main_menu = Menu(ARIAL_70, ARIAL_50)
main_menu.append_title('2D platformer')
main_menu.append_option('Start', lambda: game(level_maps[0]))
main_menu.append_option('Levels', lambda: game_menu(level_menu))
main_menu.append_option('Music', lambda: game_menu(music_menu))
main_menu.append_option('Quit', quit)

level_menu = Menu(ARIAL_70, ARIAL_50)
level_menu.append_title('Levels')
for i in range(len(level_maps)):
    level_menu.append_option('Level ' + str(i + 1), lambda: game(level_maps[i]))
level_menu.append_option('Back', lambda: game_menu(main_menu))

music_menu = Menu(ARIAL_70, ARIAL_50)
music_menu.append_title('Music volume')
music_menu.append_option('Louder', lambda: change_music_volume(0.05))
music_menu.append_option('Quieter', lambda: change_music_volume(-0.05))
music_menu.append_option('Back', lambda: game_menu(main_menu))

gameover_message = Menu(ARIAL_70, ARIAL_50)
gameover_message.append_title('Game Over')
gameover_message.append_option('Start again', lambda: game(level_maps[0]))
gameover_message.append_option('Back to menu', lambda: game_menu(main_menu))

next_level_message = Menu(ARIAL_70, ARIAL_50)
next_level_message.append_title('You have passed level')
next_level_message.append_option('Continue', lambda: game(level_maps[current_level + 1]))
next_level_message.append_option('Back to menu', lambda: game_menu(main_menu))

congratulations_message = Menu(ARIAL_70, ARIAL_50)
congratulations_message.append_title('You won! Congratulations!')
congratulations_message.append_option('Back to menu', lambda: game_menu(main_menu))

switch_scene(game_menu(main_menu))
while current_scene is not None:
    current_scene
