import pygame, random
from tiles import Tile, Objects
from settings import *
from player import Player

class Level:
    def __init__(self, level_data, surface, font, lives, current_checkpoint):
        '''
        Инициализация уровня
        :param level_data: информация о левеле (карта)
        :param surface: поверхность отрисовки уровня
        :param font: шрифт
        :param lives: количество жизней
        :param current_checkpoint: текущий чекпоинт (спавн) игрока
        '''
        self.display_surface = surface
        self.world_shift = 0
        self.on_ground = True
        self.gameover = False
        self.is_falling_death = False
        self.player_lives = lives
        self.font = font
        self.current_checkpoint = current_checkpoint
        self.checkpoints = []
        self.player_coordinates = (0, 0)
        self.finish_coordinates = (0, 0)
        self.is_finished = False
        self.colliding = False
        self.border_left = screen_width / 4
        self.border_right = screen_width - (screen_width / 4) - player_size
        self.level_data = level_data

        self.setup_level()

    def setup_level(self):
        '''
        Функция настройки карты уровня. Создает карту. Спавнит игрока, сдвигая мир на четверть ширины экрана до спавна:
        X - тайл
        G - трава
        F - дверь, являющаяся концом уровня
        P - спавн игрока (чекпоинты)
        '''
        self.tiles = pygame.sprite.Group()
        self.objects = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(self.level_data):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    control = self.control_neighbours(self.level_data, row_index, col_index)
                    tile_sprite = Tile((x,y), control)
                    self.tiles.add(tile_sprite)

                elif cell == 'G':
                    grass_sprite = Objects((x, y), random.randint(0, 2))
                    self.objects.add(grass_sprite)

                elif cell == 'F':
                    self.finish_coordinates = (x, y)
                    finish_sprite = Objects((x, y + 20), 4)
                    self.objects.add(finish_sprite)

                elif cell == 'P':
                    self.checkpoints.append((x, y))
                    checkpoint_sprite = Objects((x, y), 3)
                    self.objects.add(checkpoint_sprite)

        self.checkpoints = sorted(self.checkpoints, key = lambda i: (i[0], i[1]))

        self.tiles.update(self.border_left - self.checkpoints[self.current_checkpoint][0])
        self.objects.update(self.border_left - self.checkpoints[self.current_checkpoint][0])

        x_player = self.checkpoints[self.current_checkpoint][0]
        y_player = self.checkpoints[self.current_checkpoint][1]
        self.player_coordinates = (x_player, y_player)

        player_sprite = Player((self.border_left, y_player), self.player_lives)
        self.player.add(player_sprite)

    def control_neighbours(self, layout, row_index, col_index):
        '''
        Функция, которая проверяет наличие тайлов сверху, снизу, слева и справа от данного тайла
        :param layout: поверхность уровня
        :param row_index: ряд тайла
        :param col_index: столбец тайла
        :return: строка, состоящая из нулей или единиц (0 - тайл в данном направлении отсутствует, 1 - тайл в данном направлении присутсвует), направления - верх, низ, лево, право. Если блока не существует в каком-либо направлении, значени данного направления равно единице.
        '''
        if row_index - 1 < 0 or layout[row_index - 1][col_index] == 'X':
            b_up = '1'
        else:
            b_up = '0'
        if row_index + 1 >= len(layout) or layout[row_index + 1][col_index] == 'X':
            b_down = '1'
        else:
            b_down = '0'
        if col_index - 1 < 0 or layout[row_index][col_index - 1] == 'X':
            b_left = '1'
        else:
            b_left = '0'
        if col_index + 1 >= len(layout[row_index]) or layout[row_index][col_index + 1] == 'X':
            b_right = '1'
        else:
            b_right = '0'

        control = b_up + b_down + b_left + b_right
        return control


    def scroll_x(self):
        '''
        Функция движения либо экрана (в первой и четвертой четвертях экрана, игрок при этом не двигается), либо игрока (во второй и третьей четвертях экрана).
        '''
        player = self.player.sprite
        player_x = player.rect.x
        direction_x = player.direction.x

        if player_x < self.border_left and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
            player.rect.x = self.border_left

            if player.moving and not self.colliding:
                x_global = self.player_coordinates[0] - self.world_shift / 2
            else:
                x_global = self.player_coordinates[0]

        elif player_x > self.border_right and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
            player.rect.x = self.border_right
            if player.moving and not self.colliding:
                x_global = self.player_coordinates[0] - self.world_shift / 2
            else:
                x_global = self.player_coordinates[0]

        else:
            self.world_shift = 0
            player.speed = 8
            if player.moving and not self.colliding:
                x_global = self.player_coordinates[0] + (player.speed * direction_x) / 2

            else:
                x_global = self.player_coordinates[0]

        y_global = player.rect.y
        self.player_coordinates = (x_global, y_global)

    def horizontal_movement_collision(self):
        '''
        Функция проверки столкновения игрока с тайлами карты по горизонтали (слева и справа)
        '''
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        collision_counter = 0

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                collision_counter += 1
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

        if collision_counter > 0:
            self.colliding = True
        else:
            self.colliding = False

    def vertical_movement_collision(self):
        '''
        Функция проверки столкновения игрока с тайлами карты по вертикали (пол, потолок)
        '''
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def set_checkpoint(self):
        '''
        Функция установки нужного чекпоинта, в случае преодоления его
        :return: Возвращает номер текущего чекпоинта
        '''
        x_player = self.player_coordinates[0]
        y_player = self.player_coordinates[1]
        current_checkpoint = self.current_checkpoint
        for i in range(self.current_checkpoint + 1, len(self.checkpoints)):
            x_checkpoint = self.checkpoints[i][0]
            y_checkpoint = self.checkpoints[i][1]

            if x_checkpoint - player_size < x_player < x_checkpoint + tile_size and y_checkpoint < y_player < y_checkpoint + tile_size:
                current_checkpoint = i
        return current_checkpoint

    def check_finish(self):
        '''
        Функция проверки завершения прохождения уровня, в случае преодоления финиша (дверь)
        :return: Возвращает True, если игрок находится в финише (дверь). В остальных случаях False
        '''
        x_player = self.player_coordinates[0]
        y_player = self.player_coordinates[1]

        x_finish = self.finish_coordinates[0]
        y_finish = self.finish_coordinates[1]
        if x_finish - player_size < x_player < x_finish + tile_size and y_finish < y_player < y_finish + tile_size:
            return True
        else:
            return False

    def falling_death(self):
        '''
        Функция смерти игрока от падения в пропость
        :return: Возвращает True, если игрок упал в пропость. В остальных случаях False
        '''
        player = self.player.sprite
        if player.rect.y > screen_height + tile_size * 6:
            return True
        else:
            return False

    def show_lives(self):
        '''
        Функция отображения количество жизней (отрисовывает на экране надпись Lives: и количество оставшихся жизней)
        '''

        lives = self.font.render("Lives: " + str(self.player_lives), True, (255, 255, 255))
        lives_rect = lives.get_rect()
        lives_rect.topleft = (10, 10)
        self.display_surface.blit(lives, lives_rect)

    def run(self):
        '''
        Функция запуска уровня
        '''
        # тайлы
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        self.tiles.update(self.world_shift)

        # объекты
        self.objects.draw(self.display_surface)
        self.objects.update(self.world_shift)
        self.scroll_x()

        # игрок
        self.gameover = self.player.sprite.get_death()
        self.is_falling_death = self.falling_death()
        self.current_checkpoint = self.set_checkpoint()
        self.is_finished = self.check_finish()
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        # отрисовка
        self.show_lives()
