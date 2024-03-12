import pygame

# Variable de capacité (par défaut)
d_max_life = 3 # Vies au totales
d_max_jump = 3 # depuis la dernière plateforme
d_tick_delay_jump = 22

class hitbox:
    def __init__ (self, hitboxType:str, reference_x:int, reference_y:int, size_x:float, size_y:float, color:tuple = (0, 0, 0), srcImg=None, canJump:bool=False) :
        self.start_x = reference_x # DEBUG
        self.start_y = reference_y # DEBUG
        self.size_x = int(size_x)
        self.size_y = int(size_y)
        self.color = color
        self.srcImg = srcImg

        self.reference_x = reference_x
        self.reference_y = reference_y

        self.type = hitboxType

        self.canJump = canJump
        self.tick_start_jump = -1
        self.tick_end_jump = -1
        self.num_jump = d_max_jump
        self.remainingLife = d_max_life

        self.lookDirection = 0
        """
        0 : Regarde vers la droite
        1 : Regarde vers la gauche
        """

        self.tick_fall = 0

    
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
    
    def set_tick_fall (self, value:int) :
        self.tick_fall = value
    def get_tick_fall (self) -> int :
        return self.tick_fall
    def get_remainingLife(self) -> int :
        return self.remainingLife

    def set_lookDirection (self, newDir:int) :
        self.lookDirection = newDir
    
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
    
    def check_jump_without_num(self, currentTick:int) -> bool:
        if self.tick_end_jump <= currentTick:
            return True
        return False

    def create_jump (self, currentTick:int):
        if self.check_jump(currentTick):
            self.tick_start_jump = currentTick
            self.tick_end_jump = currentTick + d_tick_delay_jump
            self.num_jump -= 1

    def reset_num_jump(self):
        self.num_jump = d_max_jump

    def jumpExecute(self, currentTick:int, reference, PYGAME_SPEED):
        if self.canJump and self.tick_end_jump >= currentTick:
            jumpSpeed = -PYGAME_SPEED * 2 * (self.tick_end_jump - currentTick) / (self.tick_end_jump - self.tick_start_jump)
            
            if reference.every_collision(self, 'h'):
                # Quelque chose bloc le sprite par le haut, on arrête de sauter
                self.tick_end_jump = currentTick - 1
            else:
                self.move_start_y(jumpSpeed)

    def affiche(self, screen):

        if self.srcImg == None :
            pygame.draw.rect(screen, self.color, (self.start_x, self.start_y, self.size_x, self.size_y))
        else :
            image = pygame.image.load(self.srcImg[self.lookDirection])
            image = pygame.transform.scale(image, (self.size_x, self.size_y))
            screen.blit(image, (self.start_x, self.start_y))
    
    def smartShowObject(self, screen, pixel_x, block_y):
        self.start_x = pixel_x
        self.start_y = self.reference_y * block_y - block_y/2
        self.affiche(screen)
    
    def isDeath(self, PYGAME_HEIGHT):
        if self.start_y >= PYGAME_HEIGHT*1.2:
            self.remainingLife -= 1
            return True
        return False

    def relive(self, PYGAME_HEIGHT) :
        self.start_y = PYGAME_HEIGHT*0.2
        self.num_jump = d_max_jump