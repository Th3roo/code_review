import pygame
from internal.config import IMAGE_PATHS, SOUND_PATHS

"""
This module provides functions for loading game assets, including images and sounds.
It uses the pygame library for asset loading and handling.
"""

def load_images():
    """
    Loads all game images.

    This function iterates over the IMAGE_PATHS dictionary, loads each image
    using pygame.image.load(), and stores it in a dictionary. If an image
    cannot be loaded, a placeholder surface is created.

    @return: A dictionary where keys are image names and values are pygame.Surface objects.
    """
    images = {}
    for name, path in IMAGE_PATHS.items():
        try:
            images[name] = pygame.image.load(path).convert_alpha() # convert_alpha для прозрачности
        except pygame.error as e:
            print(f"Не удалось загрузить изображение {path}: {e}")
            images[name] = pygame.Surface((50,50))
            images[name].fill((255,0,255))
    return images

def load_sounds():
    """
    Loads all game sounds.

    This function iterates over the SOUND_PATHS dictionary, loads each sound
    using pygame.mixer.Sound(), and stores it in a dictionary. Sounds named
    'music' are skipped as they are handled separately.

    @return: A dictionary where keys are sound names and values are pygame.mixer.Sound objects.
    """
    sounds = {}
    for name, path in SOUND_PATHS.items():
        if name == 'music':
            continue
        try:
            sounds[name] = pygame.mixer.Sound(path)
        except pygame.error as e:
            print(f"Не удалось загрузить звук {path}: {e}")
    return sounds

def load_and_play_music():
    """
    Loads and plays background music.

    This function loads the music specified by SOUND_PATHS['music'] and
    plays it indefinitely using pygame.mixer.music.
    """
    try:
        pygame.mixer.music.load(SOUND_PATHS['music'])
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Не удалось загрузить или воспроизвести музыку {SOUND_PATHS['music']}: {e}")