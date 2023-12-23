# Importer les bibliothèques
import pygame
import time

# Importer nos classes (cl)
from cl_hitbox import hitbox



# Initialiser pygame
pygame.init()

SCREEN_RATIO = 1
PYGAME_WIDTH = 800*SCREEN_RATIO
PYGAME_HEIGHT = PYGAME_WIDTH*0.8
PYGAME_SPEED = 5*SCREEN_RATIO

# Créer un objet écran avec une largeur de 800 pixels et une hauteur de 600 pixels
screen = pygame.display.set_mode((PYGAME_WIDTH, PYGAME_HEIGHT))

# Donner un titre à la fenêtre
pygame.display.set_caption("Super Barrio Brosse")



# On créé nos objets
Player = hitbox(400, 300, PYGAME_WIDTH*0.05, PYGAME_HEIGHT*0.07, (0, 0, 255), True)
Floor = hitbox(0, (PYGAME_HEIGHT - PYGAME_HEIGHT*0.2), PYGAME_WIDTH, PYGAME_HEIGHT*0.2, (100, 75, 25))



# Créer une variable pour contrôler la boucle principale
running = True
tick = 0

# Créer une boucle principale
while running:

    # Remplir l'écran avec la couleur souhaitée
    screen.fill((200, 150, 50))

    # Dessiner les hitboxs
    Floor.affiche(screen, tick)
    Player.affiche(screen, tick, PYGAME_SPEED)

    # Mettre à jour l'affichage de l'écran
    pygame.display.flip()

    if Player.check_collision(Floor):
        Player.set_color((0, 0, 255))
        Player.num_jump = 3 # DEBUG TEST
    else :
        Player.set_color((255, 0, 0))

    # Récupérer l'état des touches du clavier
    keys = pygame.key.get_pressed()

    # Si la touche fléchée gauche est pressée, déplacer le carré vers la gauche
    if keys[pygame.K_q]:
        Player.move_start_x(-PYGAME_SPEED)
    # Si la touche fléchée droite est pressée, déplacer le carré vers la droite
    if keys[pygame.K_d]:
        Player.move_start_x(PYGAME_SPEED)
    # Si la touche fléchée haut est pressée, déplacer le carré vers le haut
    if keys[pygame.K_z]:
        Player.move_start_y(-PYGAME_SPEED)
    # Si la touche fléchée bas est pressée, déplacer le carré vers le bas
    if keys[pygame.K_s]:
        if Player.check_collision(Floor):
            pass
        else :
            Player.move_start_y(PYGAME_SPEED)
    if keys[pygame.K_SPACE]:
        Player.create_jump(tick)

    # Gérer les événements
    for event in pygame.event.get():
        # Si l'événement est de type QUIT, sortir de la boucle
        if event.type == pygame.QUIT:
            running = False

    time.sleep(0.01)
    tick += 1



# Quitter pygame
pygame.quit()




