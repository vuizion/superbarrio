import pygame

# Variable de capacité (par défaut) 
d_max_life = 3 # Vies au totales
d_max_jump = 3 # depuis la dernière plateforme
d_tick_delay_jump = 22

class hitbox:
    def __init__ (self, ref, hitboxType:str, reference_x:int, reference_y:int, size_x:float, size_y:float, color:tuple = (0, 0, 0), srcImg:list=None, canJump:bool=False, gapX:float=0, spawnPoint:bool=False) :
        
        """
        Initialise une instance de la classe 'hitbox'.

        :param game_reference: Objet du référentiel stockant cette hitbox

        :param hitboxType: Quel objet du jeu cette hitbox est censé représenter ?
        :type hitboxType: String

        :param reference_x: Nombre de cases d'abscisse, à l'horizontale, où est placé cet objet dans la map. 0 est à gauche.
        :type reference_x: Integer
        :param reference_y: Nombre de cases d'ordonné, à la verticale, où est placé cet objet dans la map. 0 est en haut.
        :type reference_y: Integer

        :param size_x: Taille en largeur de l'élément.
        :type size_x: Floating
        :param size_y: Taille en hauteur de l'élément.
        :type size_y: Floating

        :param color: Dans le cas où aucune image n'est chargée pour l'objet, on affiche une couleur à l'emplacement de la hitbox. Le format à respecter est RGB : (255, 255, 255)
        :type color: Tuple
        :param srcImg: Sources d'une ou plusieurs images impérativement en STRING enregistrées dans une tableau LIST.
        :type srcImg: List

        :param canJump: Par défaut en False, cette option active les méthodes permettant à l'objet de sauter.
        :type canJump: Boolean

        :param gapX: Un possible décallage de l'objet sur l'axe des abscisses, où l'unité est le nombre de pixel de la référence de X (exemple : 80px)
        :type gapX: Floating
        """

        self.game_reference = ref

        self.start_x = reference_x # DEBUG
        self.start_y = reference_y # DEBUG
        self.size_x = int(size_x)
        self.size_y = int(size_y)
        self.color = color
        self.srcImg = srcImg

        self.gapX = gapX # Un possible décallage de l'objet sur l'axe des abscisses, où l'unité est le nombre de pixel de la référence de X (exemple : 80px)
        self.reference_x = reference_x
        self.reference_y = reference_y

        self.type = hitboxType
        self.spawnPoint = spawnPoint

        self.canJump = canJump
        self.tick_start_jump = -1
        self.tick_end_jump = -1
        self.num_jump = d_max_jump
        self.remainingLife = d_max_life
        self.outsideMap = False # Si le personnnage meurt, on le "sort" de la map

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
        self.start_x = pixel_x + self.gapX
        self.start_y = self.reference_y * block_y - block_y/2

        if self.spawnPoint: 
            self.lookDirection = 1 if (self.game_reference.currentSpawnPoint == self.reference_x) else 0

        self.affiche(screen)
    
    def isDeath(self, PYGAME_HEIGHT):
        if not self.isOutsideMap() and (self.start_y >= PYGAME_HEIGHT*1.2):
            self.remainingLife -= 1
            self.start_y -= PYGAME_HEIGHT*0.1
            self.outsideMap = True
            return True
        return False

    def relive(self, PYGAME_HEIGHT) :
        if self.remainingLife >= 1:
            self.start_y = self.game_reference.block_y * 4
            self.start_x = self.game_reference.block_x * 4
            self.num_jump = d_max_jump
            self.outsideMap = False

    def alive(self):
        """
        Renvoit un booléan VRAI si le personnege est encore en vie
        Cela ne veut pas dire qu'il est forcément dans le jeu :
        - Utilisez dans ce cas isOutsideMap()
        """
        return self.remainingLife >= 1
    
    def isOutsideMap(self):
        """
        Renvoit un booléen VRAI si le personnage est visible à l'écran, sinon FAUX
        """
        return self.outsideMap
    
    def aiShow(self, screen, pixel_x):
        self.start_x = pixel_x
        self.affiche(screen)