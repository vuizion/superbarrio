# Importer les bibliothèques
import pygame
import time

# Importer nos classes (cl)
from cl_hitbox import hitbox
from cl_reference import reference



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
Game = reference()
Game.add_moving_as('playable', hitbox(200, 300, PYGAME_WIDTH*0.05, PYGAME_HEIGHT*0.07, (0, 0, 255), True))
Game.add_fixed_as('solid', hitbox(0, (PYGAME_HEIGHT - PYGAME_HEIGHT*0.2), PYGAME_WIDTH, PYGAME_HEIGHT*0.2, (100, 75, 25)))
Game.add_fixed_as('pierceable', hitbox(500, (PYGAME_HEIGHT - PYGAME_HEIGHT/3), PYGAME_WIDTH/6, PYGAME_HEIGHT*0.04, (100, 75, 25)))


# Créer une variable pour contrôler la boucle principale
running = True
tick = 0

# Créer une boucle principale
while running:

    # Remplir l'écran avec la couleur souhaitée
    screen.fill((200, 150, 50))

    # Dessiner les hitboxs
    Game.get_fixed_as('solid')[0].affiche(screen, tick)
    Game.get_moving_as('playable')[0].affiche(screen, tick, PYGAME_SPEED)
    Game.get_fixed_as('pierceable')[0].affiche(screen, tick)

    # Mettre à jour l'affichage de l'écran
    pygame.display.flip()

    # Récupérer l'état des touches du clavier
    keys = pygame.key.get_pressed()

    # Si la touche fléchée gauche est pressée, déplacer le carré vers la gauche
    if keys[pygame.K_q]:
        Game.get_moving_as('playable')[0].move_start_x(-PYGAME_SPEED)
    # Si la touche fléchée droite est pressée, déplacer le carré vers la droite
    if keys[pygame.K_d]:
        Game.get_moving_as('playable')[0].move_start_x(PYGAME_SPEED)
    # Si la touche fléchée haut est pressée, déplacer le carré vers le haut
    if keys[pygame.K_z]:
        Game.get_moving_as('playable')[0].move_start_y(-PYGAME_SPEED)
    # Si la touche fléchée bas est pressée, déplacer le carré vers le bas
    if keys[pygame.K_s]:
        if Game.get_moving_as('playable')[0].check_collision(Game.get_fixed_as('solid')[0]):
            pass
        else :
            Game.get_moving_as('playable')[0].move_start_y(PYGAME_SPEED)
    if keys[pygame.K_SPACE]:
        Game.get_moving_as('playable')[0].create_jump(tick)

    # Gérer les événements
    for event in pygame.event.get():
        # Si l'événement est de type QUIT, sortir de la boucle
        if event.type == pygame.QUIT:
            running = False

    Game.gravity(tick)

    time.sleep(0.01)
    tick += 1



# Quitter pygame
pygame.quit()




