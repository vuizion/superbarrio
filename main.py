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
PYGAME_SPEED = 4*SCREEN_RATIO

# Créer un objet écran avec une largeur de 800 pixels et une hauteur de 600 pixels
screen = pygame.display.set_mode((PYGAME_WIDTH, PYGAME_HEIGHT))

# Donner un titre à la fenêtre
pygame.display.set_caption("Super Barrio Brosse")



# On créé nos objets
Game = reference()
Game.add_moving_as('playable', hitbox(PYGAME_WIDTH/12, (PYGAME_HEIGHT/3)*1.8, PYGAME_WIDTH*0.065, PYGAME_HEIGHT*0.1, (0, 0, 255), ["img/p1r.png", "img/p1l.png"], True))
Game.add_fixed_as('pierceable', hitbox((PYGAME_WIDTH/4), (PYGAME_HEIGHT - (PYGAME_HEIGHT/3)*1.1), PYGAME_WIDTH/6, PYGAME_HEIGHT*0.03, (100, 75, 25)))
Game.add_fixed_as('pierceable', hitbox((PYGAME_WIDTH/3), (PYGAME_HEIGHT - (PYGAME_HEIGHT/3)*1.7), PYGAME_WIDTH/6, PYGAME_HEIGHT*0.03, (100, 75, 25)))
Game.add_fixed_as('solid', hitbox((PYGAME_WIDTH/3*2), (PYGAME_HEIGHT - PYGAME_HEIGHT/2.6), PYGAME_WIDTH/9, PYGAME_HEIGHT*0.2, (120, 120, 120), ["img/spike.png"]))



# Exemple de map
# 0 : case vide
# 1 : Élémént sol
# 1.1 : Élément sol plus grand (4x4)
# 2 : Mur
# 3 : Plateforme

map = [ [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 2, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0] ]

case_width = PYGAME_WIDTH/10
case_height = PYGAME_HEIGHT/8

for colone_id in range(len(map)):
    current_x = case_width*colone_id
    for case_id in range(len(map[colone_id])):
        case = map[colone_id][case_id]
        current_y = (case_height*case_id)-(case_height/2)
        if case == 0:
            pass
        elif case == 1:
            Game.add_fixed_as('solid', hitbox(current_x, current_y, case_width, case_height, (100, 75, 25), ["img/sand.png"]))
        elif case == 1.1:
            Game.add_fixed_as('solid', hitbox(current_x, current_y, case_width*2, case_height*2, (100, 75, 25), ["img/sand.png"]))
        elif case == 2:
            Game.add_fixed_as('solid', hitbox(current_x, current_y, case_width, case_height, (120, 120, 120)))
        elif case == 3:
            Game.add_fixed_as('solid', hitbox(current_x, current_y, case_width, case_height, (120, 120, 120)))



# Créer une variable pour contrôler la boucle principale
running = True
tick = 0


# Créer une boucle principale
while running:

    # Remplir l'écran avec la couleur souhaitée
    screen.fill((200, 150, 50))

    # Afficher les éléments en fonction de leur hitbox
    Game.showCurrentElement(PYGAME_WIDTH, screen, tick, PYGAME_SPEED)

    # Mettre à jour l'affichage de l'écran
    pygame.display.flip()

    # Récupérer l'état des touches du clavier
    keys = pygame.key.get_pressed()

    # Si la touche fléchée gauche est pressée, déplacer le carré vers la gauche
    if keys[pygame.K_q]:
        if Game.every_collision(Game.get_moving_as('playable')[0], 'g'):
            pass
        elif Game.get_moving_as('playable')[0].get_start_x() <= PYGAME_WIDTH/5:
            Game.mapScroll(True, PYGAME_SPEED)
            Game.get_moving_as('playable')[0].move_start_x(-PYGAME_SPEED) # On déplace quand même le joueur
            Game.get_moving_as('playable')[0].set_lookDirection(1)
        else:
            Game.get_moving_as('playable')[0].move_start_x(-PYGAME_SPEED)
            Game.get_moving_as('playable')[0].set_lookDirection(1)
    # Si la touche fléchée droite est pressée, déplacer le carré vers la droite
    if keys[pygame.K_d]:
        if Game.every_collision(Game.get_moving_as('playable')[0], 'd'):
            pass
        elif Game.get_moving_as('playable')[0].get_start_x() + Game.get_moving_as('playable')[0].get_size_x() >= 4*PYGAME_WIDTH/5:
            Game.mapScroll(False, PYGAME_SPEED)
            Game.get_moving_as('playable')[0].move_start_x(PYGAME_SPEED) # On déplace quand même le joueur
            Game.get_moving_as('playable')[0].set_lookDirection(0)
        else:
            Game.get_moving_as('playable')[0].move_start_x(PYGAME_SPEED)
            Game.get_moving_as('playable')[0].set_lookDirection(0)
    # Si la touche fléchée bas est pressée, déplacer le carré vers le bas
    if keys[pygame.K_s]:
        if Game.goDown(Game.get_moving_as('playable')[0]):
            Game.get_moving_as('playable')[0].move_start_y(PYGAME_SPEED)
        else :
            pass

    if keys[pygame.K_SPACE]:
        Game.get_moving_as('playable')[0].create_jump(tick)

    if keys[pygame.K_e]:
        Game.mapScroll(False, PYGAME_SPEED)

    if keys[pygame.K_a]:
        Game.mapScroll(True, PYGAME_SPEED)

    # Gérer les événements
    for event in pygame.event.get():
        # Si l'événement est de type QUIT, sortir de la boucle
        if event.type == pygame.QUIT:
            running = False

    Game.gravity(tick, PYGAME_SPEED)

    time.sleep(0.003)
    tick += 1



# Quitter pygame
pygame.quit()




