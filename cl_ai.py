import random

class ai:
    def __init__(self, block_x, hitbox, spawn_x_ref) -> None:
        self.stock_hitbox = hitbox
        self.block_x = block_x

        self.spawn_x_ref = spawn_x_ref # Point de spawn situé sur un block X de la map
        self.relative_move_x = 0 # De combien de block l'ia s'est éloigné de son spawn
        self.move_tick = 0 # Si le tick est dans un interval donné, on continue le movement
        self.speedMove = 20 # Nombre de ticks nécessaires pour se déplacer d'une longueur de block
    
    def move(self) -> None:
        if self.move_tick == 0:
            # L'ia n'est pas encore en train de bouger
            pass
        elif self.move_tick > 0 and self.move_tick < self.speedMove:
            # L'ia est en cours de déplacement vers la droite
            pass
        elif self.move_tick < 0 and self.move_tick > -self.speedMove:
            # L'ia est en cours de déplacement vers la gauche
            pass
        else:
            self.move_tick = 0

    def show(self, screen) -> None:
        self.stock_hitbox.affiche(screen)
    
    
