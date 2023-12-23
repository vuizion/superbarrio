import pygame

# Variable de capacité (par défaut)
d_max_jump = 3 # depuis la dernière plateforme
d_tick_delay_jump = 30

class hitbox:
    def __init__ (self, start_x:float, start_y:float, size_x:float, size_y:float, color:tuple = (0, 0, 0), canJump:bool=False) :
        self.start_x = int(start_x)
        self.start_y = int(start_y)
        self.size_x = int(size_x)
        self.size_y = int(size_y)
        self.color = color

        self.canJump = canJump
        self.tick_start_jump = -1
        self.tick_end_jump = -1
        self.num_jump = d_max_jump
    
    def move_start_x (self, distance:int) :
        self.start_x += distance
    def move_start_y (self, distance:int) :
        self.start_y += distance

    def resize_x (self, new_size:int) :
        self.size_x = new_size
    def resize_y (self, new_size:int) :
        self.size_y = new_size
    
    def get_start_x (self) -> int :
        return self.start_x
    def get_start_y (self) -> int :
        return self.start_y
    def get_size_x (self) -> int :
        return self.size_x
    def get_size_y (self) -> int :
        return self.size_y
    
    def set_color (self, new_color:tuple) :
        self.color = new_color
    def get_color (self) -> tuple :
        return self.color
    
    def rect(self):
        return pygame.Rect(self.start_x, self.start_y, self.size_x, self.size_y)
    
    def check_collision(self, other:object) -> bool:
        return self.rect().colliderect(other.rect())
    
    def check_jump(self, currentTick:int) -> bool:
        """
        On vérifie que le sprite :
        - a la capacité de sauter
        - a fait plus de la moitier du saut précedent, si les jumps se suivent
        - lui reste des sauts restant
        """
        moreThanHalfJump = False
        if self.tick_start_jump + int((self.tick_end_jump - self.tick_start_jump) / 2) <= currentTick:
            moreThanHalfJump = True

        if (self.canJump) and (moreThanHalfJump) and (self.num_jump > 0):
            return True
        return False

    def create_jump (self, currentTick:int):
        if self.check_jump(currentTick):
            self.tick_start_jump = currentTick
            self.tick_end_jump = currentTick + d_tick_delay_jump
            self.num_jump -= 1

    
    def affiche(self, screen, currentTick:int, PYGAME_SPEED=0):
        if self.canJump and self.tick_end_jump >= currentTick:
            jumpSpeed = -PYGAME_SPEED * (self.tick_end_jump - currentTick) / (self.tick_end_jump - self.tick_start_jump)
            self.move_start_y(jumpSpeed)

        pygame.draw.rect(screen, self.color, (self.start_x, self.start_y, self.size_x, self.size_y))
