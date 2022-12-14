import pygame, sys
from settings import *
from level import Level
from menu import Menu

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

ARIAL_50 = font.SysFont('arial', 50)

pygame.mixer.init()
pygame.mixer.music.load("music/main.mp3")
pygame.mixer.music.set_volume(0.00)
pygame.mixer.music.play(-1)

def switch_scene(scene):
    global current_scene
    current_scene = scene
def menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    main_menu.switch(-1)
                if event.key == pygame.K_DOWN:
                    main_menu.switch(1)
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    switch_scene(main_menu.select())
        screen.fill(pygame.color.THECOLORS['black'])
        main_menu.draw(screen, 500, 250, 100)
        pygame.display.update()

def music():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    music_menu.switch(-1)
                if event.key == pygame.K_DOWN:
                    music_menu.switch(1)
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    switch_scene(music_menu.select())
        screen.fill(pygame.color.THECOLORS['black'])
        music_menu.draw(screen, 500, 250, 100)
        pygame.display.update()

def change_music_volume(vol):
    volume = pygame.mixer.music.get_volume() + vol
    if 0 <= volume <= 1:
        pygame.mixer.music.unpause()
        pygame.mixer.music.set_volume(volume)
    elif volume < 0:
        pygame.mixer.music.pause()
        pygame.mixer.music.set_volume(0)

def levels():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    level_menu.switch(-1)
                if event.key == pygame.K_DOWN:
                    level_menu.switch(1)
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    switch_scene(level_menu.select())
        screen.fill(pygame.color.THECOLORS['black'])
        level_menu.draw(screen, 500, 250, 100)
        pygame.display.update()

def game_over():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    switch_scene(gameover_message.select())
        screen.fill(pygame.color.THECOLORS['black'])
        gameover_message.draw(screen, 500, 400, 100)
        pygame.display.update()

def game(level_map, lives, current_checkpoint):
    level = Level(level_map, screen, ARIAL_50, lives, current_checkpoint)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    switch_scene(menu())

        if level.is_falling_death:
            switch_scene(game(level_map, lives - 1, level.current_checkpoint))

        if level.gameover:
            switch_scene(game_over())

        screen.fill(pygame.color.THECOLORS['lightblue1'])
        level.run()
        pygame.display.update()
        clock.tick(30)

main_menu = Menu(ARIAL_50)
main_menu.append_option('Start', lambda: game(level_map1, 3, 0))
main_menu.append_option('Levels', levels)
main_menu.append_option('Music', music)
main_menu.append_option('Quit', quit)

level_menu = Menu(ARIAL_50)
level_menu.append_option('Level 1', lambda: game(level_map1, 3, 0))
level_menu.append_option('Level 2', lambda: game(level_map2, 3, 0))
level_menu.append_option('Back', menu)

music_menu = Menu(ARIAL_50)
music_menu.append_option('Louder', lambda: change_music_volume(0.05))
music_menu.append_option('Quieter', lambda: change_music_volume(-0.05))
music_menu.append_option('Back', menu)

gameover_message = Menu(ARIAL_50)
gameover_message.append_option('Game Over', menu)

switch_scene(menu())
while current_scene is not None:
    current_scene