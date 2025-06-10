import pygame
import random
from internal.config import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPEED, MOB_SPEED_MIN, MOB_SPEED_MAX

class Mob(pygame.sprite.Sprite):
    def __init__(self, mob_image):
        super().__init__()
        self.image = mob_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(MOB_SPEED_MIN, MOB_SPEED_MAX)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self, player_image, initial_lives):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20 # немного от низа
        self.lives = initial_lives

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.centerx = mouse_x

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_image, x, y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()