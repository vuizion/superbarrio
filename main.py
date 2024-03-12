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
PYGAME_SPEED = 3.8*SCREEN_RATIO

# Est-ce qu'un deuxième joueur souhaite jouer ?
multiplayer = True

# Créer un objet écran avec une largeur de 800 pixels et une hauteur de 600 pixels
screen = pygame.display.set_mode((PYGAME_WIDTH, PYGAME_HEIGHT))

# Donner un titre à la fenêtre
pygame.display.set_caption("Super Barrio Brosse")

clock = pygame.time.Clock()



# On créé nos objets
Game = reference(multiplayer, SCREEN_RATIO)
Game.add_moving_as('playable', hitbox('playable', PYGAME_WIDTH/12, (PYGAME_HEIGHT/3)*1.8, PYGAME_WIDTH*0.065, PYGAME_HEIGHT*0.1, (0, 0, 255), ["img/p1r.png", "img/p1l.png"], True))
if multiplayer : Game.add_moving_as('playable', hitbox('playable', PYGAME_WIDTH/5, (PYGAME_HEIGHT/3)*1.8, PYGAME_WIDTH*0.065, PYGAME_HEIGHT*0.1, (0, 0, 255), ["img/p2r.png", "img/p2l.png"], True))
# Game.add_fixed_as('solid', hitbox((PYGAME_WIDTH/3*2), (PYGAME_HEIGHT - PYGAME_HEIGHT/2.6), PYGAME_WIDTH/9, PYGAME_HEIGHT*0.2, (120, 120, 120), ["img/spike.png"]))


# Exemple de map
# 0 : case vide
# 1 : Élémént sol (1x2)
# 1.1 : Élément sol plus grand (2x2)
# 2 : Bloc solide
# 2.2 : Mur de 2 blocs de hauteur
# 2.3 : Mur de 3 blocs de hauteur
# 2.4 : Mur de 4 blocs de hauteur
# 3 : Plateforme d'un bloc de large

map = [ [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 3, 3, 0, 1.1, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2.3, 0, 0, 1.1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 1.1, 0],
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


# ATH
# Game.add_ath_as('text', hitbox((PYGAME_WIDTH/2), (PYGAME_HEIGHT/2.6), 2*case_width, 2*case_height, (120, 120, 120), ["img/spike.png"]))
Game.add_ath_as('background', hitbox('background', 0, 0 , 10*case_width, 8*case_height, (120, 120, 120), ["img/bg.png"]))

Game.add_ath_as('heart', hitbox('heart', 0.2*case_width, 0.2*case_height, 0.5*case_width, 0.5*case_height, (120, 120, 120), ["img/heart.png"]))
Game.add_ath_as('heart', hitbox('heart', 0.8*case_width, 0.2*case_height, 0.5*case_width, 0.5*case_height, (120, 120, 120), ["img/heart.png"]))
Game.add_ath_as('heart', hitbox('heart', 1.4*case_width, 0.2*case_height, 0.5*case_width, 0.5*case_height, (120, 120, 120), ["img/heart.png"]))

if multiplayer :
    Game.add_ath_as('heart', hitbox('heart', 8.1*case_width, 0.2*case_height, 0.5*case_width, 0.5*case_height, (120, 120, 120), ["img/heart.png"]))
    Game.add_ath_as('heart', hitbox('heart', 8.7*case_width, 0.2*case_height, 0.5*case_width, 0.5*case_height, (120, 120, 120), ["img/heart.png"]))
    Game.add_ath_as('heart', hitbox('heart', 9.3*case_width, 0.2*case_height, 0.5*case_width, 0.5*case_height, (120, 120, 120), ["img/heart.png"]))

bg = pygame.image.load("img/bg.png")
# Redimensionner l'image
bg = pygame.transform.scale(bg, (10*case_width, 8*case_height))

"""
for colone_id in range(len(map)):
    current_x = case_width*colone_id
    for case_id in range(len(map[colone_id])):
        case = map[colone_id][case_id]
        current_y = (case_height*case_id)-(case_height/2)
        if case == 0:
            pass
        elif case == 1:
            Game.add_fixed_as('solid', hitbox(current_x, current_y, case_width, case_height*2, (100, 75, 25), ["img/sol1x2.png"]))
        elif case == 1.1:
            Game.add_fixed_as('solid', hitbox(current_x, current_y, case_width*2, case_height*2, (100, 75, 25), ["img/sol2x2.png"]))
        elif case == 2:
            Game.add_fixed_as('solid', hitbox(current_x, current_y, case_width, case_height, (120, 120, 120)))
        elif case == 2.2:
            Game.add_fixed_as('solid', hitbox(current_x, current_y, case_width, case_height*2, (120, 120, 120)))
        elif case == 2.3:
            Game.add_fixed_as('solid', hitbox(current_x, current_y, case_width, case_height*3, (120, 120, 120)))
        elif case == 2.4:
            Game.add_fixed_as('solid', hitbox(current_x, current_y, case_width, case_height*4, (120, 120, 120)))
        elif case == 3:
            Game.add_fixed_as('pierceable', hitbox(current_x, current_y+(5*case_height)/6, case_width, case_height/6, (0, 120, 120)))
"""


# Créer une variable pour contrôler la boucle principale
running = True
tick = 0


# Créer une boucle principale
while running:

    # Remplir l'écran avec la couleur souhaitée
    screen.fill((200, 150, 50))
    screen.blit(bg, (0,0))

    # DEBUG AFFICHER LE BACKGROUND
    # Game.get_ath_as('background')[0].affiche(screen, tick, Game, PYGAME_SPEED)

    # Récupérer l'état des touches du clavier
    keys = pygame.key.get_pressed()



    ########################
    ##      PLAYER 1      ##
    ########################

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

    if (keys[pygame.K_SPACE] or keys[pygame.K_z]):
        Game.get_moving_as('playable')[0].create_jump(tick)




    ########################
    ##      PLAYER 2      ##
    ########################

    # Si la touche fléchée gauche est pressée, déplacer le carré vers la gauche
    if keys[pygame.K_LEFT] and multiplayer:
        if Game.every_collision(Game.get_moving_as('playable')[1], 'g'):
            pass
        elif Game.get_moving_as('playable')[1].get_start_x() <= PYGAME_WIDTH/5:
            Game.mapScroll(True, PYGAME_SPEED)
            Game.get_moving_as('playable')[1].move_start_x(-PYGAME_SPEED) # On déplace quand même le joueur
            Game.get_moving_as('playable')[1].set_lookDirection(1)
        else:
            Game.get_moving_as('playable')[1].move_start_x(-PYGAME_SPEED)
            Game.get_moving_as('playable')[1].set_lookDirection(1)

    # Si la touche fléchée droite est pressée, déplacer le carré vers la droite
    if keys[pygame.K_RIGHT] and multiplayer:
        if Game.every_collision(Game.get_moving_as('playable')[1], 'd'):
            pass
        elif Game.get_moving_as('playable')[1].get_start_x() + Game.get_moving_as('playable')[1].get_size_x() >= 4*PYGAME_WIDTH/5:
            Game.mapScroll(False, PYGAME_SPEED)
            Game.get_moving_as('playable')[1].move_start_x(PYGAME_SPEED) # On déplace quand même le joueur
            Game.get_moving_as('playable')[1].set_lookDirection(0)
        else:
            Game.get_moving_as('playable')[1].move_start_x(PYGAME_SPEED)
            Game.get_moving_as('playable')[1].set_lookDirection(0)

    # Si la touche fléchée bas est pressée, déplacer le carré vers le bas
    if keys[pygame.K_DOWN] and multiplayer:
        if Game.goDown(Game.get_moving_as('playable')[1]):
            Game.get_moving_as('playable')[1].move_start_y(PYGAME_SPEED)
        else :
            pass

    if (keys[pygame.K_UP] or keys[pygame.K_RSHIFT]) and multiplayer:
        Game.get_moving_as('playable')[1].create_jump(tick)
        







    


    # Gérer les événements
    for event in pygame.event.get():
        # Si l'événement est de type QUIT, sortir de la boucle
        if event.type == pygame.QUIT:
            running = False

    Game.gravity(tick, PYGAME_SPEED)

    # Éléments à éxécuter moins souvent
    if tick%10 == 0:
        Game.checkDeath(PYGAME_HEIGHT, screen, tick, PYGAME_SPEED)


    # Afficher les éléments en fonction de leur hitbox
    if tick%2 == 0:
        Game.smartShow(screen)
        Game.showCurrentElement(PYGAME_WIDTH, screen, tick, PYGAME_SPEED)
        # Mettre à jour l'affichage de l'écran
        pygame.display.flip()


    clock.tick(90)
    tick += 1



# Quitter pygame
pygame.quit()




