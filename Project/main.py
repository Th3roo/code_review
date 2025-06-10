import pygame
import random
import time

pygame.init()

screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Война с инопланетянами")


background_image = pygame.image.load('Project/Background.png')
player_image = pygame.image.load('Project/player.png')
mob_image = pygame.image.load('Project/mob.png')
bullet_image = pygame.image.load('Project/Bullet.png')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

pygame.mixer.music.load('Project/phon.mp3')
pygame.mixer.music.play(-1)
shoot_sound = pygame.mixer.Sound('Project/laster.mp3')
explosion_sound = pygame.mixer.Sound('Project/explosion.wav')

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = mob_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 4)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > screen_height:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = screen_height - 60
        self.lives = 3

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.x = mouse_x - self.rect.width // 2
        self.rect.y = mouse_y - self.rect.height // 2
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > screen_height - self.rect.height:
            self.rect.y = screen_height - self.rect.height

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


def show_start_screen():
    screen.blit(background_image, (0, 0))
    font = pygame.font.SysFont(None, 55)
    text = font.render('Добро пожаловать', True, BLACK)
    rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    screen.blit(text, rect)

    
    button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 50, 200, 50)
    pygame.draw.rect(screen, GRAY, button_rect)
    button_text = font.render('Играть', True, BLACK)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)

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

def show_end_screen(score):
    screen.blit(background_image, (0, 0))
    font = pygame.font.SysFont(None, 55)
    text1 = font.render('Вы проиграли!', True, BLACK)
    text2 = font.render(f'Счёт: {score}', True, BLACK)
    rect1 = text1.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    rect2 = text2.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text1, rect1)
    screen.blit(text2, rect2)

    button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 100, 300, 50)
    pygame.draw.rect(screen, GRAY, button_rect)
    button_text = font.render('Играть заново', True, BLACK)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)

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
        

def game():
   
    mob_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()

    player = Player()
    player_group.add(player)

    mob_spawn_time = 500
    last_mob_spawn_time = pygame.time.get_ticks()

    running = True
    clock = pygame.time.Clock()
    score = 0
    font = pygame.font.SysFont(None, 36)

    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                shoot_sound.play()
                bullet = Bullet(player.rect.x + player.rect.width // 2, player.rect.y)
                bullet_group.add(bullet)

        if current_time - last_mob_spawn_time > mob_spawn_time:
            mob = Mob()
            mob_group.add(mob)
            last_mob_spawn_time = current_time

        mob_group.update()
        player_group.update()
        bullet_group.update()

        for bullet in bullet_group:
            mob_hit_list = pygame.sprite.spritecollide(bullet, mob_group, True)
            for mob in mob_hit_list:
                explosion_sound.play()
                bullet.kill()
                score += 1

        mob_hit_list = pygame.sprite.spritecollide(player, mob_group, True)
        for mob in mob_hit_list:
            player.lives -= 1
            if player.lives == 0:
                running = False

        screen.blit(background_image, (0, 0))
        mob_group.draw(screen)
        player_group.draw(screen)
        bullet_group.draw(screen)

        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, [10, 10])

        lives_text = font.render(f'Lives: {player.lives}', True, BLACK)
        screen.blit(lives_text, [10, 40])

        pygame.display.flip()
        clock.tick(60)

    return score

playing = True
while playing:
    if not show_start_screen():
        break
    score = game()
    if not show_end_screen(score):
        break

pygame.quit()