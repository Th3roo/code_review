import pygame
from internal.config import IMAGE_PATHS, SOUND_PATHS

def load_images():
    """Загружает все игровые изображения."""
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
    """Загружает все игровые звуки."""
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
    """Загружает и запускает фоновую музыку."""
    try:
        pygame.mixer.music.load(SOUND_PATHS['music'])
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Не удалось загрузить или воспроизвести музыку {SOUND_PATHS['music']}: {e}")