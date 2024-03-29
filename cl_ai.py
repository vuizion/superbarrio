import random

class ai:
    def __init__(self, ref, block_x, hitbox, spawn_x_ref) -> None:
        self.game_reference = ref

        self.stock_hitbox = hitbox
        self.block_x = block_x

        self.spawn_x_ref = spawn_x_ref # Point de spawn situé sur un block X de la map

        self.relative_move_x = 0 # De combien de block l'ia s'est éloigné de son spawn
        self.max_block = 3 
        
        self.move_tick = 0 # Si le tick est dans un interval donné, on continue le movement
        self.speedMove = 30 # Nombre de ticks nécessaires pour se déplacer d'une longueur de block
        self.realSpeed = self.block_x/self.speedMove

        self.relative_pixel_x = 0 # Nombre de pixel dont l'ia s'est déplacée à partir du spawn

    def get_spawn_x(self):
        return self.spawn_x_ref
    
    def get_ai_hitbox(self):
        return self.stock_hitbox
    
    def move(self) -> None:
        if self.move_tick == 0:
            # L'ia n'est pas encore en train de bouger

            # On vérifie si elle ne s'est pas trop éloigné d'abord
            if self.relative_move_x >= self.max_block:
                self.move_tick -= 1
            elif self.relative_move_x <= -self.max_block:
                self.move_tick += 1

            if random.randint(0,1) == 1:
                self.move_tick += 1
                self.relative_pixel_x += self.realSpeed
            else:
                self.move_tick -= 1
                self.relative_pixel_x -= self.realSpeed
        elif self.move_tick > 0 and self.move_tick < self.speedMove:
            # L'ia est en cours de déplacement vers la droite
            self.move_tick += 1
            self.relative_pixel_x += self.realSpeed
        elif self.move_tick < 0 and self.move_tick > -self.speedMove:
            # L'ia est en cours de déplacement vers la gauche
            self.move_tick -= 1
            self.relative_pixel_x -= self.realSpeed
        else:
            if self.move_tick > 0:
                self.relative_move_x += 1
            else :
                self.relative_move_x -= 1

            self.move_tick = 0

    def show(self, screen, pixel_x, PYGAME_WIDTH) -> None:

        # On vérifie que l'ia est à l'ecran avant de la faire bouger
        if self.stock_hitbox.get_start_x() < PYGAME_WIDTH:
            self.move()

        self.game_reference.ia_collision(self, "d")
        self.stock_hitbox.aiShow(screen, pixel_x+self.relative_pixel_x)
    
    
