
#Importer la bibliothèque pygame
import pygame

# Initialiser pygame
pygame.init()

# Créer un objet écran avec une largeur de 800 pixels et une hauteur de 600 pixels
screen = pygame.display.set_mode((800, 600))

# Donner un titre à la fenêtre
pygame.display.set_caption("Mon écran en Python")

# Créer une variable pour contrôler la boucle principale
running = True

# Créer une variable pour stocker la position du carré
x = 400
y = 300

# Créer une boucle principale
while running:
    # Remplir l'écran avec la couleur noire
    screen.fill((0, 0, 0))

    # Dessiner un carré bleu de 50 pixels de côté à la position (x, y)
    pygame.draw.rect(screen, (0, 0, 255), (x, y, 50, 50))

    # Mettre à jour l'affichage de l'écran
    pygame.display.flip()

    # Gérer les événements
    for event in pygame.event.get():
        # Si l'événement est de type QUIT, sortir de la boucle
        if event.type == pygame.QUIT:
            running = False
        # Si l'événement est de type KEYDOWN, modifier la position du carré
        elif event.type == pygame.KEYDOWN:
            # Si la touche est la flèche gauche, déplacer le carré vers la gauche
            if event.key == pygame.K_LEFT:
                x -= 10
            # Si la touche est la flèche droite, déplacer le carré vers la droite
            elif event.key == pygame.K_RIGHT:
                x += 10
            # Si la touche est la flèche haut, déplacer le carré vers le haut
            elif event.key == pygame.K_UP:
                y -= 10
            # Si la touche est la flèche bas, déplacer le carré vers le bas
            elif event.key == pygame.K_DOWN:
                y += 10

# Quitter pygame
pygame.quit()