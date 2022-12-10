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
    x: float
    y: float

    direction: str = ""
    speed: float = 4
    alive: bool = True
    score: int = 0

    def draw(self):
        rect = pygame.Rect(self.x, self.y, 30, 30)
        pygame.draw.rect(win, WHITE, rect)

    def update(self):
        if self.direction == "left":
            self.x -= 0
        elif self.direction == "right":
            self.x += 0

        if self.x > 370:
            self.x = 370
        elif self.x < 0:
            pass # 1.2 Faites en sorte que le joueur ne puisse pas quitter l'écran en allant trop vers la gauche

# 1.1 Changez la position initiale du joueur
player = Player(x=0, y=0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key_press = pygame.key.get_pressed()

        if key_press[pygame.K_LEFT]:
            player.direction = "left"
        elif key_press[pygame.K_RIGHT]:
            pass # 1.2 Changez la direction du joueur en fonction de la touche du clavier utilisée



    win.fill(BLACK)
    player.update()
    player.draw()
    pygame.display.update()
