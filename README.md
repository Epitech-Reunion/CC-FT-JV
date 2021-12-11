# Simple shooter - {EPITECH.} Focus Tech Jeux Video - Dec 2021

Découverte de la programmation de jeu video avec Python et Pygame

## Etape 0 - Vocabulaire de la programmation

- Variable: 
  - Une donnée de notre programme.
  - Comme son nom l'indique cette donnée peu varier au cours de l'execution du programme.
  - Exemple: la position d'un joueur
  - ``` player.x = 10 ```
- Condition:
  -  Permet d'executer une partie d'un programme sous une certaine condition.
  -  Exemple: Déplace le joueur à gauche s'il veut aller à gauche sinon déplace le joueur sur la droite s'il veut aller à droite:
    ```
    if self.direction == "left":
        self.x = self.x - 4
    elif self.direction == "right":
        self.x = self.x + 4
    ```
- Boucle:
  - Permet d'executer des actions en boucle.
  - Exemple: tant que le joueur n'a pas fermé la fenêtre du jeu, execute le code du jeu 
   - ```
     running = True
     while running:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         ...
         pygame.display.update()
     ```
- Fonction:
  - Permet de regrouper plusieurs instructions de notre programme en une seule instruction réutilisable.
  - Exemple: une fonction qui permmet au joueur de tirer une balle.
  - ```
    def shoot(self):
      if ship.alive:
          self.x = ship.x + 15
          self.y = ship.y
          self.is_shot = True
    
    ...
    
    bullet.shoot()
    ```

## Etape 1 - Positionner et déplacer des éléments:

Notions abordées:
- Variables
- Conditions

### 1.1 - Placer le vaisseau du joueur

Par défault le vaisseau du joueur se trouve en (0, 0).

Trouvez un moyen de placer le joueur en bas de l'écran.

### 1.2 - Déplacer le joueur

Vous avez réussi à placer le joueur en bas de l'écran.

Maintenant, essayez de faire en sorte que lorsque le joueur se déplace horizontalement lorsque vous appuyez sur les touches gauche et droite de votre clavier.
Le joueur ne doit pas pouvoir sortir de l'écran.

## Etape 2 - Tirer un projectile

Notion abordée:
- Créer et utiliser une fonction

### 2.1 - Faire tirer le joueur

Vous savez maintenant associer des touches de votre clavier à des évenements.
Un nouvel élement vient d'être ajouté à notre jeu: le projectile.

Lorsque le joueur appuie la touche Espace, un projectile doit être crée à l'endroit où se trouve le vaisseau.

Ce projectile doit alors traverser l'écran verticalement.
Le projectile doit être affiché uniquement lorsqu'il est tiré.

### 2.2 - Cycle de vie du projectile

Lorque le projectile quitte l'écran il ne doit plus être considéré comme tiré.

Lorsqu'il y a déjà un projectile qui se déplace à l'écran, le joueur ne doit pas pouvoir en tirer un autre.

## Etape 3 - Ajouter un ennemi

### 3.1 - Placement initial de l'ennemi

Maintenant que le vaisseau peut tirer un projectile, rajoutons un ennemi à notre jeu.

Tout comme le vaisseau, notre ennemi sera représenté par un carré et devra initialement se trouver dans le coin supérieur gauche de l'écran.

### 3.2 - Déplacement de l'ennemi

L'ennemi doit pouvoir se déplacer vers la droite jusqu'au bord droit de l'écran.

Lorsqu'il atteind le bord droit de l'écran l'ennemi devra descendre de 30 pixel vers le bas de l'écran et se déplacer cette fois-ci de la gauche vers la droite.

Lorsqu'il atteind le bord droit de l'écran l'ennemi devra aussi descendre de 30 pixel vers le bas de l'écran et reprendre un déplacement de la droite vers la gauche et ainsi de suite jusqu'à ce que l'ennemi atteigne le bas de l'écran.

## Etape 4 - Gestion des collisions

Nous avons maintenant tous les élements nécessaire à la réalisation d'un vrai jeu:

 - Un joueur (le vaisseau)
 - Des actions réalisable par le joueur (se déplacer et tirer)
 - Un ennemi

Il ne nous reste plus qu'à assembler ces différents élements pour rendre notre jeu un peu plus amusant

### 4.1 - Collision entre le tir et l'ennemi

Si la balle tirée par le joueur entre en collision avec l'ennemi, vous devez faire disparaitre l'ennemi mais aussi la balle.

### 4.2 - Collision entre le joueur et l'ennemi

Si l'ennemi touche le joueur, vous devez faire disparaitre le joueur (GAME OVER).

## Etape 5 - Score et difficulté

Donnons de l'intérêt à notre jeu en ajoutant un score et en augmentant progressivement la difficulté.

Plus le jouer réussi à tirer avec succès sur l'ennemi, plus ce dernier se déplacera vite.

Plus l'ennemi se déplace vite, plus le joueur marque de point en réussissant à le toucher.

### 5.1 - Difficulté

Si le joueur arrive à tirer sur l'ennemi: l'ennemi est remis à sa position d'origine (0, 0) et sa vitesse augmente de 1

### 5.2 - Score

Si le joueur arrive à tirer sur l'ennemi: le score du joueur devra augmenter de la valeur absolue (abs) de la vitesse de l'ennemi.

 - abs(4) = 4
 - abs(-4) = 4
 - abs(-12) = 12
 - abs(42) = 42

## Etape 6 - Bonus - Plusieurs ennemis

Essayez de rajouter plusieurs ennemis pour augmenter la difficulté du jeu.
