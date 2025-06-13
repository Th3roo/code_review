import pygame
from internal.sprites import Player, Mob, Bullet
from internal.config import (SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, PLAYER_LIVES_START,
                    MOB_SPAWN_TIME_MS, FONT_NAME_DEFAULT, FONT_SIZE_MEDIUM)
from internal.ui import draw_text

"""
This module contains the main game loop and related game logic.
It handles event processing, sprite updates, collision detection,
and rendering the game state to the screen.
"""

def game_loop(screen, clock, images, sounds):
    """
    Runs the main game loop.

    This function initializes the game state, including the player, mobs, and bullets.
    It handles user input, updates game objects, checks for collisions,
    and draws the game on the screen. The loop continues until the player quits
    or loses all lives.

    @param screen: The pygame.Surface object representing the game screen.
    @param clock: The pygame.time.Clock object for managing game speed.
    @param images: A dictionary of loaded game images.
    @param sounds: A dictionary of loaded game sounds.
    @return: The player's score if the game ends normally, or -1 if the player quits.
    """
    
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    player = Player(images['player'], PLAYER_LIVES_START)
    all_sprites.add(player)

    mob_spawn_timer = pygame.time.get_ticks()
    score = 0
    
    running = True
    while running:
        clock.tick(60)
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    sounds['shoot'].play()
                    bullet = Bullet(images['bullet'], player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        if current_time - mob_spawn_timer > MOB_SPAWN_TIME_MS:
            mob = Mob(images['mob'])
            all_sprites.add(mob)
            mobs.add(mob)
            mob_spawn_timer = current_time

        all_sprites.update()

        hits = pygame.sprite.groupcollide(mobs, bullets, True, True) # mob, bullet, dokill_mob, dokill_bullet
        for hit_mob in hits: # hits это словарь {mob: [bullets]}
            sounds['explosion'].play()
            score += 1

        mob_hits_player = pygame.sprite.spritecollide(player, mobs, True) # True удаляет моба при столкновении
        for hit_mob in mob_hits_player:
            # TODO add mega boom for mobs
            player.lives -= 1
            if player.lives <= 0:
                running = False

        screen.blit(images['background'], (0, 0))
        all_sprites.draw(screen)

        draw_text(screen, f'Score: {score}', FONT_SIZE_MEDIUM, 60, 20, BLACK, center_aligned=False)
        draw_text(screen, f'Lives: {player.lives}', FONT_SIZE_MEDIUM, 60, 50, BLACK, center_aligned=False)
        
        pygame.display.flip()

    pygame.mouse.set_visible(True)
    pygame.event.set_grab(False)

    return score