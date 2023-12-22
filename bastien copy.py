 # Créer un rectangle correspondant à la position de l'obstacle
        rect_obstacle = pygame.Rect(ox, oy, 100, 100)

        # Tester si le rectangle futur du carré est en collision avec le rectangle de l'obstacle
        if futur_carre.colliderect(rect_obstacle):
            # Si oui, ne pas déplacer le carré
            pass
        else:
            # Si non, déplacer le carré
            x = futur_x

    # Si la touche flèche droite est pressée, déplacer le carré vers la droite
    if touches[pygame.K_RIGHT]:
        # Calculer la position future du carré
        futur_x = x + vitesse
        futur_y = y

        # Créer un rectangle correspondant à la position future du carré
        futur_carre = pygame.Rect(futur_x, futur_y, 50, 50)

        # Créer un rectangle correspondant à la position de l'obstacle
        rect_obstacle = pygame.Rect(ox, oy, 100, 100)

        # Tester si le rectangle futur du carré est en collision avec le rectangle de l'obstacle
        if futur_carre.colliderect(rect_obstacle):
            # Si oui, ne pas déplacer le carré
            pass
        else:
            # Si non, déplacer le carré
            x = futur_x

    # Si la touche flèche haut est pressée, déplacer le carré vers le haut
    if touches[pygame.K_UP]:
        # Calculer la position future du carré
        futur_x = x
        futur_y = y - vitesse

        # Créer un rectangle correspondant à la position future du carré
        futur_carre = pygame.Rect(futur_x, futur_y, 50, 50)

        # Créer un rectangle correspondant à la position de l'obstacle
        rect_obstacle = pygame.Rect(ox, oy, 100, 100)

        # Tester si le rectangle futur du carré est en collision avec le rectangle de l'obstacle
        if futur_carre.colliderect(rect_obstacle):
            # Si oui, ne pas déplacer le carré
            pass
        else:
            # Si non, déplacer le carré
            y = futur_y

    # Si la touche flèche bas est pressée, déplacer le carré vers le bas
    if touches[pygame.K_DOWN]:
        # Calculer la position future du carré
        futur_x = x
        futur_y = y + vitesse

        # Créer un rectangle correspondant à la position future du carré
        futur_carre = pygame.Rect(futur_x, futur_y, 50, 50)

        # Créer un rectangle correspondant à la position de l'obstacle
        rect_obstacle = pygame.Rect(ox, oy, 100, 100)

        # Tester si le rectangle futur du carré est en collision avec le rectangle de l'obstacle
        if futur_carre.colliderect(rect_obstacle):
            # Si oui, ne pas déplacer le carré
            pass
        else:
            # Si non, déplacer le carré
            y = futur_y

    # Effacer la fenêtre
    fenetre.fill((0, 0, 0))

    # Afficher le carré à sa nouvelle position
    fenetre.blit(carre, (x, y))

    # Afficher l'obstacle
    fenetre.blit(obstacle, (ox, oy))

    # Mettre à jour l'affichage
    pygame.display.flip()

















import pygame

# Initialiser pygame
pygame.init()

# Créer une fenêtre de 800x600 pixels
fenetre = pygame.display.set_mode((800, 600))

# Donner un titre à la fenêtre
pygame.display.set_caption("Déplacement avec les flèches et collision")

# Créer un carré rouge de 50x50 pixels
carre = pygame.Surface((50, 50))
carre.fill((255, 0, 0))

# Définir la position initiale du carré au centre de la fenêtre
x = 375
y = 275

# Créer un obstacle bleu de 100x100 pixels
obstacle = pygame.Surface((100, 100))
obstacle.fill((0, 0, 255))

# Définir la position de l'obstacle
ox = 200
oy = 200

# Créer une horloge pour contrôler la fréquence d'affichage
horloge = pygame.time.Clock()

# Créer une variable pour la boucle principale
continuer = True

# Boucle principale
while continuer:
    # Limiter la fréquence d'affichage à 60 images par seconde
    horloge.tick(60)

    # Gérer les événements
    for event in pygame.event.get():
        # Si l'utilisateur ferme la fenêtre, quitter le programme
        if event.type == pygame.QUIT:
            continuer = False

    # Récupérer l'état des touches du clavier
    touches = pygame.key.get_pressed()

    # Définir la vitesse de déplacement du carré
    vitesse = 5

    # Si la touche flèche gauche est pressée, déplacer le carré vers la gauche
    if touches[pygame.K_LEFT]:
        # Calculer la position future du carré
        futur_x = x - vitesse
        futur_y = y

        # Créer un rectangle correspondant à la position future du carré
        futur_carre = pygame.Rect(futur_x, futur_y, 50, 50)

        # Créer un rectangle correspondant à la position de l'obstacle
        rect_obstacle = pygame.Rect(ox, oy, 100, 100)

        # Tester si le rectangle futur du carré est en collision avec le rectangle de l'obstacle
        if futur_carre.colliderect(rect_obstacle):
            # Si oui, ne pas déplacer le carré
            pass
        else:
            # Si non, déplacer le carré
            x = futur_x

    # Si la touche flèche droite est pressée, déplacer le carré vers la droite
    if touches[pygame.K_RIGHT]:
        # Calculer la position future du carré
        futur_x = x + vitesse
        futur_y = y

        # Créer un rectangle correspondant à la position future du carré
        futur_carre = pygame.Rect(futur_x, futur_y, 50, 50)

        # Créer un rectangle correspondant à la position de l'obstacle
        rect_obstacle = pygame.Rect(ox, oy, 100, 100)

        # Tester si le rectangle futur du carré est en collision avec le rectangle de l'obstacle
        if futur_carre.colliderect(rect_obstacle):
            # Si oui, ne pas déplacer le carré
            pass
        else:
            # Si non, déplacer le carré
            x = futur_x

    # Si la touche flèche haut est pressée, déplacer le carré vers le haut
    if touches[pygame.K_UP]:
        # Calculer la position future du carré
        futur_x = x
        futur_y = y - vitesse

        # Créer un rectangle correspondant à la position future du carré
        futur_carre = pygame.Rect(futur_x, futur_y, 50, 50)

        # Créer un rectangle correspondant à la position de l'obstacle
        rect_obstacle = pygame.Rect(ox, oy, 100, 100)

        # Tester si le rectangle futur du carré est en collision avec le rectangle de l'obstacle
        if futur_carre.colliderect(rect_obstacle):
            # Si oui, ne pas déplacer le carré
            pass
        else:
            # Si non, déplacer le carré
            y = futur_y

    # Si la touche flèche bas est pressée, déplacer le carré vers le bas
    if touches[pygame.K_DOWN]:
        # Calculer la position future du carré
        futur_x = x
        futur_y = y + vitesse

        # Créer un rectangle correspondant à la position future du carré
        futur_carre = pygame.Rect(futur_x, futur_y, 50, 50)

        # Créer un rectangle correspondant à la position de l'obstacle
        rect_obstacle = pygame.Rect(ox, oy, 100, 100)

        # Tester si le rectangle futur du carré est en collision avec le rectangle de l'obstacle
        if futur_carre.colliderect(rect_obstacle):
            # Si oui, ne pas déplacer le carré
            pass
        else:
            # Si non, déplacer le carré
            y = futur_y

    # Effacer la fenêtre
    fenetre.fill((0, 0, 0))

    # Afficher le carré à sa nouvelle position
    fenetre.blit(carre, (x, y))

    # Afficher l'obstacle
    fenetre.blit(obstacle, (ox, oy))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter pygame
pygame.quit()
