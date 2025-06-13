import pygame
from internal.config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, GRAY, FONT_NAME_DEFAULT, FONT_SIZE_LARGE

"""
This module provides functions for creating and displaying User Interface (UI) elements.
It includes functions for drawing text, and showing start and end game screens.
"""

def draw_text(surface, text, size, x, y, color, font_name=FONT_NAME_DEFAULT, center_aligned=True):
    """
    Draws text on a given surface.

    This utility function renders text using a specified font and color,
    and blits it onto the provided surface at the given coordinates.

    @param surface: The pygame.Surface to draw the text on.
    @param text: The string of text to draw.
    @param size: The font size.
    @param x: The x-coordinate for the text position.
    @param y: The y-coordinate for the text position.
    @param color: The color of the text (RGB tuple).
    @param font_name: The name of the font to use (defaults to FONT_NAME_DEFAULT).
    @param center_aligned: Boolean indicating if the text should be centered at (x, y).
                           If False, (x, y) is the top-left corner.
    @return: The pygame.Rect object representing the bounds of the rendered text.
    """
    font = pygame.font.SysFont(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center_aligned:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x,y)
    surface.blit(text_surface, text_rect)
    return text_rect

def show_start_screen(screen, background_image):
    """
    Displays the start screen of the game.

    This function shows a welcome message and a "Play" button. It waits for
    player input (either closing the window or clicking the button).

    @param screen: The pygame.Surface object representing the game screen.
    @param background_image: The pygame.Surface to use as the background.
    @return: True if the player clicks "Play", False if the player quits.
    """
    screen.blit(background_image, (0, 0))
    draw_text(screen, 'Добро пожаловать', FONT_SIZE_LARGE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, BLACK)
    
    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50)
    pygame.draw.rect(screen, GRAY, button_rect)
    draw_text(screen, 'Играть', FONT_SIZE_LARGE, button_rect.centerx, button_rect.centery, BLACK)

    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if button_rect.collidepoint(mouse_x, mouse_y):
                    return True
    return False

def show_end_screen(screen, background_image, score):
    """
    Displays the end screen of the game.

    This function shows a "Game Over" message, the player's final score,
    and a "Play Again" button. It waits for player input.

    @param screen: The pygame.Surface object representing the game screen.
    @param background_image: The pygame.Surface to use as the background.
    @param score: The player's final score to display.
    @return: True if the player clicks "Play Again", False if the player quits.
    """
    screen.blit(background_image, (0, 0))
    draw_text(screen, 'Вы проиграли!', FONT_SIZE_LARGE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 70, BLACK)
    draw_text(screen, f'Счёт: {score}', FONT_SIZE_LARGE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20, BLACK)

    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 70, 300, 50)
    pygame.draw.rect(screen, GRAY, button_rect)
    draw_text(screen, 'Играть заново', FONT_SIZE_LARGE, button_rect.centerx, button_rect.centery, BLACK)
    
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if button_rect.collidepoint(mouse_x, mouse_y):
                    return True
    return False