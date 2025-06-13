import pygame
import sys
import os

# Экран
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
GAME_TITLE = "Война с инопланетянами"

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

ASSET_BASE_PATH = 'assets/'

# Проверяем, запущен ли скрипт из PyInstaller
if getattr(sys, 'frozen', False):
    # Если да, используем путь к временной директории, созданной PyInstaller
    ASSET_BASE_PATH = os.path.join(sys._MEIPASS, 'assets') + os.sep
else:
    # Иначе, используем обычный относительный путь (для разработки)
    ASSET_BASE_PATH = 'assets' + os.sep


IMAGE_PATHS = {
    'background': ASSET_BASE_PATH + 'Background.png',
    'player': ASSET_BASE_PATH + 'player.png',
    'mob': ASSET_BASE_PATH + 'mob.png',
    'bullet': ASSET_BASE_PATH + 'Bullet.png'
}

SOUND_PATHS = {
    'music': ASSET_BASE_PATH + 'phon.mp3',
    'shoot': ASSET_BASE_PATH + 'laster.mp3',
    'explosion': ASSET_BASE_PATH + 'explosion.wav'
}

FONT_NAME_DEFAULT = None
FONT_SIZE_LARGE = 55
FONT_SIZE_MEDIUM = 36

PLAYER_LIVES_START = 3
MOB_SPAWN_TIME_MS = 500
BULLET_SPEED = -10
MOB_SPEED_MIN = 2
MOB_SPEED_MAX = 4