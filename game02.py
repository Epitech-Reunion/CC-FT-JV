import pygame
from dataclasses import dataclass
from pygame.constants import KEYDOWN

pygame.init()
clock = pygame.time.Clock()

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
    x: float
    y: float

    direction: str = ""
    speed: float = 400
    alive: bool = True
    score: int = 0

    def draw(self):
        rect = pygame.Rect(self.x, self.y, 30, 30)
        pygame.draw.rect(win, WHITE, rect)

    def update(self):
        if self.alive:
            if self.direction == "left":
                self.x -= self.speed * dt
            elif self.direction == "right":
                self.x += self.speed * dt

            if self.x > 370:
                self.x = 370
            if self.x < 0:
                self.x = 0

@dataclass()
class Bullet():
    x: float
    y: float
    is_shot: bool = False
    speed: float = 400

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
            self.y -= self.speed * dt

@dataclass
class Enemy():
    x: int
    y: int
    color: tuple = RED
    speed: float = 200
    alive: bool = True

    def draw(self):
        if self.alive:
            rect = pygame.Rect(self.x, self.y, 30, 30)
            pygame.draw.rect(win, self.color, rect)

    def update(self):
        # 2.2 Ajoutez le pattern de déplacement de l'ennemi 
        pass

player = Player(x=200, y=550)
bullet = Bullet(x=200, y=550)
# 2.1 Placement initial de l'ennemi en début de partie

running = True
while running:
    dt = clock.tick(60)/1000
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
    # 2.1 N'oubliez pas de mettre à jour l'état de l'ennemi et de le dessiner à l'écran
    pygame.display.update()
