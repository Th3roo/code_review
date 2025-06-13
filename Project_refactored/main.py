import pygame
import internal.config as config
import internal.asset_loader as asset_loader
import internal.ui as ui
import internal.game_logic as game_logic

"""
This module is the main entry point for the game.
It initializes pygame, loads assets, and manages the overall game flow,
including displaying start/end screens and running the main game loop.
"""

def main():
    """
    Main function to run the game.

    Initializes pygame and its mixer, sets up the game window,
    loads assets (images and sounds), and then enters the main application loop.
    This loop handles showing the start screen, running the game logic,
    and showing the end screen, allowing the player to restart or quit.
    """
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption(config.GAME_TITLE)
    clock = pygame.time.Clock()

    try:
        images = asset_loader.load_images()
        sounds = asset_loader.load_sounds()
        asset_loader.load_and_play_music()
    except Exception as e:
        print(f"Критическая ошибка при загрузке ресурсов: {e}")
        pygame.quit()
        return

    app_running = True
    while app_running:
        if not ui.show_start_screen(screen, images['background']):
            app_running = False # Пользователь закрыл окно или выбрал выход
            break
        
        score = game_logic.game_loop(screen, clock, images, sounds)

        if score == -1: # Если пользователь вышел из игры во время game_loop
             app_running = False
             break

        # Показываем экран конца игры
        # Функция должна возвращать True для рестарта, False для выхода
        if not ui.show_end_screen(screen, images['background'], score):
            app_running = False # Пользователь закрыл окно или выбрал выход
            break
        # Если True, цикл app_running начнется заново со стартового экрана

    pygame.quit()

if __name__ == '__main__':
    main()