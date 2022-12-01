import pygame
from tiles import AnimatedTile
import random

class Enemy(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, 'graphics/enemy/move')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = -0.01

    def move(self):
        self.rect.x += self.speed

    def reverse_image(self):
        '''if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)
        else:'''
        self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self):
        self.speed *= -1

    def update(self):
        self.rect.x += self.speed
        self.animate()
        self.move()
        #self.reverse_image()