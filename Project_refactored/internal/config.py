import pygame
import sys
import os

"""
This module defines configuration variables for the game.
It includes settings for screen dimensions, frame rate, game title, colors,
asset paths, font settings, and gameplay parameters.
"""

# Screen configuration
SCREEN_WIDTH = 400  # Width of the game screen in pixels
SCREEN_HEIGHT = 600  # Height of the game screen in pixels
FPS = 60  # Frames per second for the game loop
GAME_TITLE = "Война с инопланетянами"  # Title of the game window

# Color definitions (RGB tuples)
WHITE = (255, 255, 255)  # White color
BLACK = (0, 0, 0)  # Black color
RED = (255, 0, 0)  # Red color
GREEN = (0, 255, 0)  # Green color
BLUE = (0, 0, 255)  # Blue color
GRAY = (128, 128, 128)  # Gray color

# Asset base path configuration
ASSET_BASE_PATH = 'assets/'  # Default base path for assets

# Check if the script is running from PyInstaller
if getattr(sys, 'frozen', False):
    # If yes, use the path to the temporary directory created by PyInstaller
    ASSET_BASE_PATH = os.path.join(sys._MEIPASS, 'assets') + os.sep
else:
    # Otherwise, use the regular relative path (for development)
    ASSET_BASE_PATH = 'assets' + os.sep

# Image asset paths
IMAGE_PATHS = {
    'background': ASSET_BASE_PATH + 'Background.png',  # Path to the background image
    'player': ASSET_BASE_PATH + 'player.png',  # Path to the player sprite
    'mob': ASSET_BASE_PATH + 'mob.png',  # Path to the mob sprite
    'bullet': ASSET_BASE_PATH + 'Bullet.png'  # Path to the bullet sprite
}

# Sound asset paths
SOUND_PATHS = {
    'music': ASSET_BASE_PATH + 'phon.mp3',  # Path to the background music file
    'shoot': ASSET_BASE_PATH + 'laster.mp3',  # Path to the shooting sound effect
    'explosion': ASSET_BASE_PATH + 'explosion.wav'  # Path to the explosion sound effect
}

# Font settings
FONT_NAME_DEFAULT = None  # Default font name (None for system default)
FONT_SIZE_LARGE = 55  # Large font size
FONT_SIZE_MEDIUM = 36  # Medium font size

# Gameplay settings
PLAYER_LIVES_START = 3  # Initial number of lives for the player
MOB_SPAWN_TIME_MS = 500  # Time interval in milliseconds for mob spawning
BULLET_SPEED = -10  # Speed of bullets (negative for upward movement)
MOB_SPEED_MIN = 2  # Minimum speed for mobs
MOB_SPEED_MAX = 4  # Maximum speed for mobs