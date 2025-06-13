import pygame
import random
from internal.config import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPEED, MOB_SPEED_MIN, MOB_SPEED_MAX

"""
This module defines sprite classes for game objects.
It includes classes for Mobs (enemies), the Player, and Bullets.
These classes inherit from pygame.sprite.Sprite and handle their
own appearance, movement, and behavior.
"""

class Mob(pygame.sprite.Sprite):
    """
    Represents an enemy mob in the game.

    Attributes:
        image (pygame.Surface): The image of the mob.
        rect (pygame.Rect): The rectangular area of the mob.
        speed (int): The vertical speed of the mob.
    """
    def __init__(self, mob_image):
        """
        Initializes a new Mob instance.

        @param mob_image: The pygame.Surface to use as the mob's image.
        """
        super().__init__()
        self.image = mob_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(MOB_SPEED_MIN, MOB_SPEED_MAX)

    def update(self):
        """
        Updates the mob's position.
        The mob moves downwards, and if it goes off the bottom of the screen,
        it is removed from all sprite groups.
        """
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

class Player(pygame.sprite.Sprite):
    """
    Represents the player character in the game.

    Attributes:
        image (pygame.Surface): The image of the player.
        rect (pygame.Rect): The rectangular area of the player.
        lives (int): The number of lives the player has.
    """
    def __init__(self, player_image, initial_lives):
        """
        Initializes a new Player instance.

        @param player_image: The pygame.Surface to use as the player's image.
        @param initial_lives: The starting number of lives for the player.
        """
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20 # немного от низа
        self.lives = initial_lives

    def update(self):
        """
        Updates the player's position based on mouse movement.
        The player's horizontal position is controlled by the mouse,
        and it is kept within the screen boundaries.
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.centerx = mouse_x

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        
class Bullet(pygame.sprite.Sprite):
    """
    Represents a bullet fired by the player.

    Attributes:
        image (pygame.Surface): The image of the bullet.
        rect (pygame.Rect): The rectangular area of the bullet.
        speed (int): The vertical speed of the bullet.
    """
    def __init__(self, bullet_image, x, y):
        """
        Initializes a new Bullet instance.

        @param bullet_image: The pygame.Surface to use as the bullet's image.
        @param x: The initial x-coordinate of the bullet's center.
        @param y: The initial y-coordinate of the bullet's bottom.
        """
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = BULLET_SPEED

    def update(self):
        """
        Updates the bullet's position.
        The bullet moves upwards, and if it goes off the top of the screen,
        it is removed from all sprite groups.
        """
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()