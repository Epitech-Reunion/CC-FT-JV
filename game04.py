import pygame
from dataclasses import dataclass
from pygame.constants import KEYDOWN

pygame.init()

# Notre fenêtre de jeu aura une dimenssion de 400x600 pixels
win = pygame.display.set_mode((400, 600))

pygame.display.set_caption("{EPITECH.}-Reunion-FocusTech-JV")
font = pygame.font.SysFont(None, 24)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

@dataclass
class Player():
    x: int
    y: int

    direction: str = ""
    speed: int = 4
    alive: bool = True
    score: int = 0

    def draw(self):
        if self.alive:
            rect = pygame.Rect(self.x, self.y, 30, 30)
            pygame.draw.rect(win, WHITE, rect)
        score_text = font.render(f'Score: {self.score}', True, WHITE)
        win.blit(score_text, (0, 560))

    def update(self):
        if self.alive:
            if self.direction == "left":
                self.x -= self.speed
            elif self.direction == "right":
                self.x += self.speed

            if self.x > 370:
                self.x = 370
            if self.x < 0:
                self.x = 0

@dataclass()
class Bullet():
    x: int
    y: int
    is_shot: bool = False
    speed: int = 4

    def shoot(self):
        if player.alive:
            self.x = player.x + 15
            self.y = player.y
            self.is_shot = True

    def draw(self):
        if self.is_shot:
            rect = pygame.Rect(self.x, self.y, 5, 15)
            pygame.draw.rect(win, WHITE, rect)

    def update(self):
        if self.y < 0:
            self.is_shot = False
        if self.is_shot:
            self.y -= self.speed

@dataclass
class Enemy():
    x: int
    y: int
    color: tuple = RED
    speed: int = 2
    alive: bool = True

    def draw(self):
        if self.alive:
            rect = pygame.Rect(self.x, self.y, 30, 30)
            pygame.draw.rect(win, self.color, rect)

    def update(self):
        if self.alive:
            if self.x > 430:
                self.y += 30
                self.speed = -self.speed
            if self.x < -30:
                self.y += 30
                self.speed = -self.speed
            if self.y > 630:
                self.speed = 0
            self.x += self.speed

    def collide_with_ship(self):
        if self.alive:
            enemy_rect = pygame.Rect(self.x, self.y, 30, 30)
            ship_rect = pygame.Rect(player.x, player.y, 30, 30)
            return enemy_rect.colliderect(ship_rect)

    def collide_with_bullet(self):
        if self.alive and bullet.is_shot:
            enemy_rect = pygame.Rect(self.x, self.y, 30, 30)
            bullet_rect = pygame.Rect(bullet.x, bullet.y, 5, 15)
            return enemy_rect.colliderect(bullet_rect)

player = Player(x=200, y=550)
bullet = Bullet(x=200, y=550)
enemy = Enemy(x=0, y=0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key_press = pygame.key.get_pressed()

        if key_press[pygame.K_LEFT]:
            player.direction = "left"
        elif key_press[pygame.K_RIGHT]:
            player.direction = "right"
        else:
            player.direction = ""
        if key_press[pygame.K_SPACE] and not bullet.is_shot:
            bullet.shoot()

    win.fill(BLACK)
    player.update()
    player.draw()
    bullet.update()
    bullet.draw()
    enemy.update()
    enemy.draw()
    if enemy.collide_with_ship():
        player.alive = False
    if enemy.collide_with_bullet():
        bullet.is_shot = False
        # 4 Augmentez le score du joueur et la vitesse de l'ennemi
        # N'oubliez pas de replacer l'ennemi à sa position initiale en (0, 0)
    pygame.display.update()
