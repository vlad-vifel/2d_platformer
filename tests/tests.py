import pygame
from level import Level

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


def test_control_neighbours1():
    res = test_level.control_neighbours(test_map, 1, 1)
    assert res == '1101'


def test_control_neighbours2():
    res = test_level.control_neighbours(test_map, 0, 2)
    assert res == '1111'


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
    x_player = test_level4.player_coordinates[0]
    y_player = test_level4.player_coordinates[1]
    test_level4.player_coordinates = (x_player, y_player)
    assert test_level4.falling_death() == False


def test_get_status():
    player.sprite.direction.x = 0
    player.get_status()
    assert player.status == 'run'
