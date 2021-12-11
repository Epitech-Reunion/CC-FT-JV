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
        rect = pygame.Rect(self.x, self.y, 30, 30)
        pygame.draw.rect(win, WHITE, rect)

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
        # 2.1 Action a faire lorsque le joueur tire
        # Initialisez la position du projectile
        # Le projectile est tiré

    def draw(self):
        if self.is_shot:
            rect = pygame.Rect(self.x, self.y, 5, 15)
            pygame.draw.rect(win, WHITE, rect)

    def update(self):
        if self.is_shot:
            # 2.1 Que fait-on dans ce cas là ?
        if self.y < 0:
            # 2.2 Que fait-on dans ce cas là ?

player = Player(x=200, y=550)
bullet = Bullet(x=200, y=550)

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

        # 2.1 Si le joueur appuie sur la touche ESPACE (inspirez-vous des conditions précédentes)

    win.fill(BLACK)
    player.update()
    player.draw()
    bullet.update()
    bullet.draw()
    pygame.display.update()
