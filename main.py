# Importer les bibliothèques
import pygame

# Importer nos classes (cl)
from cl_hitbox import hitbox
from cl_reference import reference


# Initialiser pygame
pygame.init()

SCREEN_RATIO = 1
PYGAME_WIDTH = 800*SCREEN_RATIO
PYGAME_HEIGHT = PYGAME_WIDTH*0.8
PYGAME_SPEED = 3.8*SCREEN_RATIO**2

# Est-ce qu'un deuxième joueur souhaite jouer ?
multiplayer = False

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




# Fond d'écran
bg = pygame.image.load("img/bg.png")
bg = pygame.transform.scale(bg, (10*case_width, 8*case_height)) # Redimensionner l'image


# Créer une variable pour contrôler la boucle principale
running = True
tick = 0



# test de l'ia
Game.addAi(5)



###########################
# Chargement de la police depuis un fichier ttf
chemin_police = "font/pixel.ttf"  # Spécifiez le chemin vers votre fichier de police
taille_police = 32
police = pygame.font.Font(chemin_police, taille_police)
###########################



# Créer une boucle principale
while running:


    # Remplir l'écran avec la couleur souhaitée
    screen.fill((200, 150, 50))
    screen.blit(bg, (0,0))

    # Récupérer l'état des touches du clavier
    keys = pygame.key.get_pressed()





    ########################
    ##      PLAYER 1      ##
    ########################

    # Si la touche fléchée gauche est pressée, déplacer le carré vers la gauche
    if keys[pygame.K_q]:
        Game.movePlayer(0,'g')

    # Si la touche fléchée droite est pressée, déplacer le carré vers la droite
    if keys[pygame.K_d]:
        Game.movePlayer(0,'d')

    # Si la touche fléchée bas est pressée, déplacer le carré vers le bas
    if keys[pygame.K_s]:
        if Game.goDown(Game.get_moving_as('playable')[0]):
            Game.get_moving_as('playable')[0].move_start_y(PYGAME_SPEED)

    if (keys[pygame.K_SPACE] or keys[pygame.K_z]):
        Game.movePlayer(0,'h', tick)



    ########################
    ##      PLAYER 2      ##
    ########################

    # Si la touche fléchée gauche est pressée, déplacer le carré vers la gauche
    if keys[pygame.K_LEFT] and multiplayer:
        Game.movePlayer(1,'g')

    # Si la touche fléchée droite est pressée, déplacer le carré vers la droite
    if keys[pygame.K_RIGHT] and multiplayer:
        Game.movePlayer(1,'d')

    # Si la touche fléchée bas est pressée, déplacer le carré vers le bas
    if keys[pygame.K_DOWN] and multiplayer:
        if Game.goDown(Game.get_moving_as('playable')[1]):
            Game.get_moving_as('playable')[1].move_start_y(PYGAME_SPEED)

    if (keys[pygame.K_UP] or keys[pygame.K_RSHIFT] or keys[pygame.K_KP0]) and multiplayer:
        Game.movePlayer(1,'h', tick)
        





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

        ###########################
        # Définition du texte
        texte_surface = police.render(Game.getScore(), True, (255, 255, 255))  # Création de la surface du texte
        # Positionnement du texte au centre de la fenêtre
        texte_rect = texte_surface.get_rect(center=(PYGAME_WIDTH/2, 0.46*case_height))
        # Affichage du texte sur la surface de la fenêtre
        screen.blit(texte_surface, texte_rect)
        ###########################

        # Mettre à jour l'affichage de l'écran
        pygame.display.flip()


    clock.tick(90)
    tick += 1



# Quitter pygame
pygame.quit()




