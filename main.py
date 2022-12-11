import pygame, sys
from settings import *
from level import Level
from menu import Menu

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

ARIAL_50 = font.SysFont('arial', 50)
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
        main_menu.draw(screen, 500, 200, 100)
        pygame.display.update()

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
        level_menu.draw(screen, 500, 200, 100)
        pygame.display.update()

def game(level_map):
    level = Level(level_map, screen, ARIAL_50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    switch_scene(menu())

        if level.gameover:
            switch_scene(menu())

        screen.fill(pygame.color.THECOLORS['lightblue1'])
        level.run()
        pygame.display.update()
        clock.tick(60)


main_menu = Menu(ARIAL_50)
main_menu.append_option('Start', lambda: game(level_map1))
main_menu.append_option('Levels', levels)
main_menu.append_option('Quit', quit)

level_menu = Menu(ARIAL_50)
level_menu.append_option('Level 1', lambda: game(level_map1))
level_menu.append_option('Level 2', lambda: game(level_map2))
level_menu.append_option('Back', menu)

switch_scene(menu())
while current_scene is not None:
    current_scene