import pygame, random
from tiles import Tile, Grass
from settings import *
from player import Player
# from enemy import Enemy

class Level:
    def __init__(self, level_data, surface, font, lives, current_checkpoint):
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
        self.spawn_coordinates = (0, 0)
        self.colliding = False
        self.was_scrolled = False

        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.grass = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        # self.enemy = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    control = self.control_neighbours(layout, row_index, col_index)
                    tile_sprite = Tile((x,y), control)
                    self.tiles.add(tile_sprite)

                if cell == 'G':
                    grass_sprite = Grass((x, y), random.randint(0,2))
                    self.grass.add(grass_sprite)

                if cell == 'P':
                    self.checkpoints.append((x, y))
                    grass_sprite = Grass((x, y), 3)
                    self.grass.add(grass_sprite)


                # if cell == 'E':
                #     enemy_sprite = Enemy(tile_size, x, y)
                #     self.enemy.add(enemy_sprite)

        self.checkpoints = sorted(self.checkpoints, key = lambda i: (i[0], i[1]))

        self.tiles.update((screen_width / 4) - self.checkpoints[self.current_checkpoint][0])
        self.grass.update((screen_width / 4) - self.checkpoints[self.current_checkpoint][0])

        x_player = self.checkpoints[self.current_checkpoint][0]
        y_player = self.checkpoints[self.current_checkpoint][1]
        self.player_coordinates = (x_player, y_player)

        player_sprite = Player((screen_width / 4, y_player), self.player_lives)
        self.player.add(player_sprite)

    def control_neighbours(self, layout, row_index, col_index):
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

        return b_up + b_down + b_left + b_right


    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.x
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
            self.was_scrolled = True
            if player.moving and not self.colliding:
                x_global = self.player_coordinates[0] - self.world_shift / 2
            else:
                x_global = self.player_coordinates[0]

            if not self.was_scrolled:
                x_global += 8 * direction_x

            self.was_scrolled = True

        elif player_x + tile_size > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
            if player.moving and not self.colliding:
                x_global = self.player_coordinates[0] - self.world_shift / 2
            else:
                x_global = self.player_coordinates[0]

            if not self.was_scrolled:
                x_global += 8 * direction_x

            self.was_scrolled = True

        else:
            self.world_shift = 0
            player.speed = 8
            if player.moving and not self.colliding:
                x_global = self.player_coordinates[0] + (player.speed * direction_x) / 2
            else:
                x_global = self.player_coordinates[0]

            if self.was_scrolled:
                x_global -= 8 * direction_x

            self.was_scrolled = False



        y_global = player.rect.y
        self.player_coordinates = (x_global, y_global)

        print(self.player_coordinates, self.world_shift, player.speed * direction_x, (-self.world_shift + player.speed * direction_x) / 2, self.colliding)
    def horizontal_movement_collision(self):
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

    def falling_death(self):
        player = self.player.sprite

        if player.rect.y > screen_height + tile_size * 6:
            return True
        else:
            return False

    # def enemy_horizontal_movement_collision(self):
    #     enemy = self.enemy.sprite
    #     enemy.rect.x += enemy.speed
    #
    #     for sprite in self.tiles.sprites():
    #         if sprite.rect.colliderect(enemy.rect):
    #             if enemy.speed < 0:
    #                 enemy.rect.left = sprite.rect.right
    #
    #             elif enemy.speed > 0:
    #                 enemy.rect.right = sprite.rect.left
    #             enemy.reverse()
    #             enemy.reverse_image()
    def show_lives(self, surf):
        lives = self.font.render("Lives: " + str(self.player_lives), True, (255, 255, 255))
        lives_rect = lives.get_rect()
        lives_rect.topleft = (10, 10)
        surf.blit(lives, lives_rect)

    def run(self):

        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # level grass
        self.grass.update(self.world_shift)
        self.grass.draw(self.display_surface)
        self.scroll_x()

        # player
        self.gameover = self.player.sprite.get_death()
        self.is_falling_death = self.falling_death()

        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        self.show_lives(self.display_surface)





        # enemy
        # self.enemy.update()
        # self.enemy.draw(self.display_surface)

