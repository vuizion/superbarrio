# Importer nos classes (cl)
from cl_obstacle import obstacle
from cl_hitbox import hitbox


class reference:
    def __init__ (self, multiplayer:bool=False, SCREEN_RATIO:float=1):
        self.moving = {
            'playable' : [],
            'ai' : [],
            'item' : []
        }
        self.fixed = {
            'solid' : [],
            'pierceable' : [],
            'enterable' : []
        }
        self.ath = {
            'background' : [],
            'text' : [],
            'heart' : []
        }
        self.elements = []

        self.loadedColumns = 0 # Stock le nombre de colonne dèjà chargées : des objets sont déjà créé et stocké juste au dessus à partir de la map composé d'élément sous forme de code
        self.leftColumn = 0 # id de la colonne la plus à gauche de l'écran
        self.leftColumnPixel = 0 # pixel séparant la gauche de la colonne avec le bord gauche de l'écran

        self.SCREEN_RATIO = SCREEN_RATIO
        self.PYGAME_WIDTH = 800*self.SCREEN_RATIO
        self.PYGAME_HEIGHT = self.PYGAME_WIDTH*0.8
        self.PYGAME_SPEED = 3.8*self.SCREEN_RATIO
        self.block_x = int(self.PYGAME_WIDTH/10)
        self.block_y = int(self.PYGAME_HEIGHT/8)

        self.multiplayer = multiplayer

        # Exemple de map
        # 0 : case vide
        # 0.1 : spawn du joueur 1
        # 0.2 : spawn du joueur 2
        # 0.3 : point de respawn pendant le parcours
        # 1 : Élémént sol (1x2)
        # 1.1 : Élément sol plus grand (2x2)
        # 2 : Bloc solide
        # 2.2 : Mur de 2 blocs de hauteur
        # 2.3 : Mur de 3 blocs de hauteur
        # 2.4 : Mur de 4 blocs de hauteur
        # 3 : Plateforme d'un bloc de large

        self.map = [[0, 0, 0, 0, 0, 0, 0, 1.1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0.1, 0, 0, 1.1, 0],
                    [0, 0, 0, 0, 0.2, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        self.obstacle = obstacle()
        self.add_obstacle()

    def showCurrentElement(self, PYGAME_WIDTH, screen, tick, PYGAME_SPEED) :
        everyObject = []
        everyObject.append(sum(self.fixed.values(), []))
        everyObject.append(sum(self.moving.values(), []))
        everyObject = sum(everyObject, [])

        for obj in everyObject:
            if obj.get_start_x() > -obj.get_size_x() and obj.get_start_x() < PYGAME_WIDTH :
                obj.affiche(screen)
        
        # Afficher le bon nombre de coeurs au bon joueur
        for heartId in range(len(self.ath['heart'])) :
            if heartId+1 <= 3 and heartId < self.moving['playable'][0].get_remainingLife() :
                self.ath['heart'][heartId].affiche(screen)
            elif heartId+1 > 3 and heartId+1 <= 6 and heartId < self.moving['playable'][1].get_remainingLife()+3 :
                self.ath['heart'][heartId].affiche(screen)

    def smartShow(self, screen) -> None:
        self.selectLeftColumn()
        firstColumn = (self.leftColumn - 1 if self.leftColumn != 0 else 0)
        for columnID in range(firstColumn, self.leftColumn + 11):
            if columnID < len(self.elements): # Notre ID existe bien dans la liste elements qui enregistre tous nos objets
                for elem in self.elements[columnID]:
                    pixel_x = self.leftColumnPixel + (columnID - self.leftColumn)*self.block_x
                    if elem != None : elem.smartShowObject(screen, pixel_x, self.block_y)

    def selectLeftColumn(self):
        if self.leftColumnPixel < -self.block_x:
            self.leftColumn += 1
            self.leftColumnPixel += self.block_x
        elif self.leftColumnPixel > 0 and self.leftColumn > 0:
            self.leftColumn -= 1
            self.leftColumnPixel -= self.block_x
        elif self.leftColumnPixel > 0 and self.leftColumn <= 0:
            self.leftColumn = 0
            self.leftColumnPixel = 0

    
    def add_moving_as(self, key:str, obj:object):
        self.moving[key].append(obj)
    def add_fixed_as(self, key:str, obj:object):
        self.fixed[key].append(obj)
    def add_ath_as(self, key:str,  obj:object):
        self.ath[key].append(obj)

    def get_moving_as(self, key:str):
        return self.moving[key]
    def get_fixed_as(self, key:str):
        return self.fixed[key]
    def get_ath_as(self, key:str):
        return self.ath[key]
    
    def gravity(self, currentTick:int, PYGAME_SPEED):
        everyMoving = sum(self.moving.values(), [])
        everyFixed = sum(self.fixed.values(), [])

        for oneMoving in everyMoving:
            oneMoving.jumpExecute(currentTick, self, PYGAME_SPEED)

            isFalling = True

            if self.every_collision(oneMoving, 'b'):
                isFalling = False

            if oneMoving.check_jump_without_num(currentTick):
                pass
            else:
                isFalling = False


            if isFalling:
                speedGravity = (currentTick - oneMoving.get_tick_fall())*0.6*(PYGAME_SPEED/4)
                if speedGravity > (9*PYGAME_SPEED/4):
                    speedGravity = (9*PYGAME_SPEED/4)

                if speedGravity > 9: # Sécurité : ne pas traverser les planchers
                    speedGravity = 9

                oneMoving.move_start_y(speedGravity)
            else :
                oneMoving.set_tick_fall(currentTick) # Puisqu'il ne tombe pas, il ne peut pas avoir commencé à tomber avant maintenant
                if oneMoving.check_jump_without_num(currentTick):
                    oneMoving.reset_num_jump()

    def goDown(self, obj:object):
        """
        Descendre d'une plateforme si elle le permet
        """
        for oneFixed in self.fixed['pierceable']:
            if obj.check_collision(oneFixed):
                if (obj.get_start_y() + obj.get_size_y() - 10) <= (oneFixed.get_start_y()):
                    return True
        return False

    def every_collision (self, obj:object, direction:str) -> int:
        everyFixed = sum(self.fixed.values(), [])

        listFixed = []
        for oneFixed in everyFixed:
            if obj.check_collision(oneFixed):
                listFixed.append(oneFixed)

        result = False

        if direction == 'b':
            for obstacle in listFixed:
                if (obj.get_start_y() + obj.get_size_y() - 10) <= (obstacle.get_start_y()):
                    result = True
        
        if direction == 'h':
            for obstacle in listFixed:
                if (obstacle.get_start_y() + obstacle.get_size_y() - 10) <= (obj.get_start_y()):
                    result = True
        
        if direction == 'd':
            for obstacle in listFixed:
                if (obj.get_start_x() + obj.get_size_x() - 10) <= (obstacle.get_start_x()):
                    if obstacle.get_start_y() < (obj.get_start_y()+obj.get_size_y()-12): # Condition ajoutée pour régler le bug "le personnage s'arrête car un seul pixel dépasse du sol"
                        result = True
        
        if direction == 'g':
            for obstacle in listFixed:
                if (obstacle.get_start_x() + obstacle.get_size_x() - 10) <= (obj.get_start_x()):
                    if obstacle.get_start_y() < (obj.get_start_y()+obj.get_size_y()-12): # Condition ajoutée pour régler le bug "le personnage s'arrête car un seul pixel dépasse du sol"
                        result = True
        
        return result
    

    def mapScroll(self, leftDirection:bool, PYGAME_SPEED, whichPlayer:object=None):
        everyObject = []
        everyObject.append(sum(self.fixed.values(), []))
        everyObject.append(sum(self.moving.values(), []))
        everyObject = sum(everyObject, [])

        for obj in everyObject:
            obj.move_start_x(PYGAME_SPEED if leftDirection else -PYGAME_SPEED)

    def checkDeath(self, PYGAME_HEIGHT, screen, tick, PYGAME_SPEED):
        for player in self.moving['playable']:
            if player.isDeath(PYGAME_HEIGHT):
                if player.get_remainingLife() >= 1 :
                    player.relive(PYGAME_HEIGHT)
                else :
                    pass
                    #print("C'est finit tu es mort")
                # self.ath['text'][0].affiche(screen, tick, self, PYGAME_SPEED)
                    
    def add_obstacle(self) -> None:
        self.map.append([0, 0, 0, 0, 0.3, 0, 0, 2.2, 0]) # Point de respawn avant l'obstacle
        for column in self.obstacle.difficulty_1_num_1():
            self.map.append(column)
        self.loadRemainingColumns()

    def loadRemainingColumns(self):
        for newColId in range(self.loadedColumns, len(self.map)):
            columnToAdd = []
            for blockId in range(len(self.map[newColId])):
                block = self.map[newColId][blockId]
                if block != 0 : columnToAdd.append(self.createRealHitbox(block, newColId, blockId))
            self.elements.append(columnToAdd)
        self.loadedColumns = len(self.map)

    def createRealHitbox(self, block:float, ref_x:int, ref_y:int) -> object:
        if block == 1:
            return hitbox('solid', ref_x, ref_y, self.block_x, self.block_y*2, (100, 75, 25), ["img/sol1x2.png"])
        elif block == 1.1:
            return hitbox('solid', ref_x, ref_y, self.block_x*2, self.block_y*2, (100, 75, 25), ["img/sol2x2.png"])
        elif block == 2.2:
            return hitbox('solid', ref_x, ref_y, self.block_x, self.block_y*2, (120, 120, 120))
        return None

