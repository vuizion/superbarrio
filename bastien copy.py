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
