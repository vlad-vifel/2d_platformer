import pygame, random
from tiles import Tile, Grass
from settings import tile_size, screen_width
from player import Player
from enemy import Enemy

class Level:
    def __init__(self, level_data, surface, font):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.on_ground = True
        self.gameover = False
        self.lives = 100000
        self.font = font

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

                if cell == 'K':
                    grass_sprite = Grass((x, y), 3)
                    self.grass.add(grass_sprite)

                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

                # if cell == 'E':
                #     enemy_sprite = Enemy(tile_size, x, y)
                #     self.enemy.add(enemy_sprite)

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
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

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
        self.player_lives = self.player.sprite.get_lives()

        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        self.show_lives(self.display_surface)





        # enemy
        # self.enemy.update()
        # self.enemy.draw(self.display_surface)

