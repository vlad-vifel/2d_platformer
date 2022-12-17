import pygame
from level import Level
from player import Player

pygame.init()
pygame.font.init()
ARIAL_50 = pygame.font.SysFont('arial', 50)
test_map = ['XXX',
            ' XX',
            'PXX',
            'X X']
test_map2 = ['XXX',
             ' XP',
             'X X']
test_map3 = ['XXXXX',
             'X   P',
             'XP  X',
             'XXXXX']
test_map4 = ['XXX',
             'XPX',
             'X X']
test_map5 = ['XXXX',
             'XPFX',
             'XXXX']
test_screen = pygame.display.set_mode((400, 320))
test_level = Level(test_map, test_screen, ARIAL_50, 3, 0)
test_level2 = Level(test_map2, test_screen, ARIAL_50, 3, 0)
test_level3 = Level(test_map3, test_screen, ARIAL_50, 3, 0)
test_level4 = Level(test_map4, test_screen, ARIAL_50, 3, 0)
test_level5 = Level(test_map5, test_screen, ARIAL_50, 3, 0)
player = Player((0, 0), 1)

# Проверка функция класса Level
def test_control_neighbours1():
    assert test_level.control_neighbours(test_map, 1, 1) == '1101'


def test_control_neighbours2():
    assert test_level.control_neighbours(test_map, 0, 2) == '1111'


def test_horizontal_movement_collision1():
    test_level.horizontal_movement_collision()
    assert test_level.colliding == False


def test_horizontal_movement_collision2():
    test_level2.player.sprite.direction.x = -1
    test_level2.horizontal_movement_collision()
    assert test_level2.colliding == True


def test_vertical_movement_collsion():
    test_level4.vertical_movement_collision()
    assert test_level4.player.sprite.on_ground == False


def test_set_checkpoint():
    x_player = test_level3.player_coordinates[0] + 240
    y_player = test_level3.player_coordinates[1] - 80
    test_level3.player_coordinates = (x_player, y_player)
    test_level3.set_checkpoint()
    assert test_level3.current_checkpoint == 1


def test_check_finish():
    x_player = test_level5.player_coordinates[0] + 64
    y_player = test_level5.player_coordinates[1]
    test_level5.player_coordinates = (x_player, y_player)
    test_level5.check_finish()
    assert test_level5.is_finished == True

def test_falling_death():
    assert test_level.falling_death() == False

def test_falling_death1():
    x_player = test_level4.player_coordinates[0]
    y_player = test_level4.player_coordinates[1] + 1000
    test_level4.player_coordinates = (x_player, y_player)
    player.rect.y = y_player
    test_level4.falling_death()
    assert test_level4.falling_death() == True

# Проверка функция класса Player
def test_get_status():
    player.direction.x = 0
    player.get_status()
    assert player.status == 'idle'

def test_get_status2():
    player.direction.x = 1
    player.get_status()
    assert player.status == 'run'

def test_get_status3():
    player.direction.y = -2
    player.get_status()
    assert player.status == 'jump'

def test_get_status4():
    player.direction.y = 2
    player.get_status()
    assert player.status == 'fall'

def test_get_death():
    player.lives = 0
    assert player.get_death() == True

def test_get_death2():
    player.lives = 3
    assert player.get_death() == False
