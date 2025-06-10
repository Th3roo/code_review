import pygame
from internal.config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, GRAY, FONT_NAME_DEFAULT, FONT_SIZE_LARGE

def draw_text(surface, text, size, x, y, color, font_name=FONT_NAME_DEFAULT, center_aligned=True):
    """Утилита для отрисовки текста."""
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