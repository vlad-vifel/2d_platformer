import pygame
from support import import_folder
class Player(pygame.sprite.Sprite):

    def __init__(self, pos: list, lives):
        '''
        Инициализация игрока
        :param pos: координаты
        :param lives: количество жизней
        '''
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 0.005
        self.gravity = 0.8
        self.jump_speed = -16
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.lives = lives
        self.moving = False

    def import_character_assets(self):
        '''
        Функция выводит ассеты персонажа, с помощью функции import_folder,
        в зависимости от действия
        '''
        character_path = 'graphics/character0/'
        self.animations = {'idle': list, 'run': list, 'jump': list, 'fall': list}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        '''
        Функция бегает по картинкам в определенной папке, создавая анимацию действий персонажа
        Так же зеркально отражает картинки в случае движения влево
        '''
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        if self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center = self.rect.center)

    def get_input(self):
        '''
        Проверяет какую кнопку нажали на клавиатуре и в соответствии с этим двигает персонажа
        Стрелочка вправо - движение впарво
        Стрелочка влево - движение влево
        Стрелочка вверх - прыжок
        '''
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
            self.moving = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
            self.moving = True
        else:
            self.direction.x = 0
            self.moving = False

        if keys[pygame.K_UP]:
            if self.on_ground:
                self.jump()

    def get_status(self):
        '''
        Изменяет значение self.status в зависимости от действия (прыжок, падение, бег, стояние на месте)
        '''
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def apply_gravity(self):
        '''
        Функция гравитации, добавляет гравитацию (притяжение вниз к блокам)
        '''
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        '''
        Функция прыжка, добавляет значение self.jump_speed к координате по вертикальной оси
        '''
        self.direction.y = self.jump_speed

    def get_death(self):
        '''
        Функция смерти проверяет количество жизней.
        :return:  В случае если жизней 0 или меньше возвращает True, В других случаях - False
        '''
        return True if self.lives <= 0 else False

    def get_lives(self):
        '''
        Функция обращается к количеству жизней
        :return: self.lives - Количество жизней
        '''
        return self.lives

    def update(self):
        '''
        Ежесекундно вызывает функции self.get_input(), self.get_status(), self.animate
        '''
        self.get_input()
        self.get_status()
        self.animate()

