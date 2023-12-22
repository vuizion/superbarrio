
#Importer la bibliothèque pygame
import pygame
import time




class hitbox:
    def __init__ (self, start_x:float, start_y:float, size_x:float, size_y:float, color:tuple = (0, 0, 0)) :
        self.start_x = int(start_x)
        self.start_y = int(start_y)
        self.size_x = int(size_x)
        self.size_y = int(size_y)
        self.color = color
    
    def move_start_x (self, distance:int) :
        self.start_x += distance
    def move_start_y (self, distance:int) :
        self.start_y += distance

    def resize_x (self, new_size:int) :
        self.size_x = new_size
    def resize_y (self, new_size:int) :
        self.size_y = new_size
    
    def get_start_x (self) :
        return self.start_x
    def get_start_y (self) :
        return self.start_y
    def get_size_x (self) :
        return self.size_x
    def get_size_y (self) :
        return self.size_y
    
    def set_color (self, new_color:tuple) :
        self.color = new_color
    def get_color (self) :
        return self.color
    
    def rect (self):
        return pygame.Rect(self.start_x, self.start_y, self.size_x, self.size_y)

def afficher_hitbox(current:object) :
    pygame.draw.rect(screen, current.get_color(), (current.get_start_x(), current.get_start_y(), current.get_size_x(), current.get_size_y()))

def check_collision(obj1: object, obj2: object) -> bool:
    rect1 = pygame.Rect(obj1.get_start_x(), obj1.get_start_y(), obj1.get_size_x(), obj1.get_size_y())
    rect2 = pygame.Rect(obj2.get_start_x(), obj2.get_start_y(), obj2.get_size_x(), obj2.get_size_y())
    return rect1.colliderect(rect2)



# Initialiser pygame
pygame.init()

SCREEN_RATIO = 1
PYGAME_WIDTH = 1000*SCREEN_RATIO
PYGAME_HEIGHT = PYGAME_WIDTH*0.8
PYGAME_SPEED = 6*SCREEN_RATIO

# Créer un objet écran avec une largeur de 800 pixels et une hauteur de 600 pixels
screen = pygame.display.set_mode((PYGAME_WIDTH, PYGAME_HEIGHT))

# Donner un titre à la fenêtre
pygame.display.set_caption("Super Barrio Brosse")



# On créé nos objets
Player = hitbox(400, 300, PYGAME_WIDTH*0.05, PYGAME_HEIGHT*0.07, (0, 0, 255))
Floor = hitbox(0, (PYGAME_HEIGHT - PYGAME_HEIGHT*0.2), PYGAME_WIDTH, PYGAME_HEIGHT*0.2, (100, 75, 25))



# Créer une variable pour contrôler la boucle principale
running = True

# Créer une boucle principale
while running:
    # Remplir l'écran avec la couleur souhaitée
    screen.fill((200, 150, 50))

    # Dessiner les hitboxs
    afficher_hitbox(Player)
    afficher_hitbox(Floor)

    # Mettre à jour l'affichage de l'écran
    pygame.display.flip()

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
        if check_collision(Player, Floor):
            pass
        else :
            Player.move_start_y(PYGAME_SPEED)

    # Gérer les événements
    for event in pygame.event.get():
        # Si l'événement est de type QUIT, sortir de la boucle
        if event.type == pygame.QUIT:
            running = False


    if check_collision(Player, Floor):
        Player.set_color((0, 0, 255))
    else :
        Player.set_color((255, 0, 0))

    time.sleep(0.01)



# Quitter pygame
pygame.quit()




