# Importer nos classes (cl)
from cl_obstacle import obstacle
from cl_hitbox import hitbox
from cl_ai import ai


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
        self.PYGAME_SPEED = 3.8*self.SCREEN_RATIO**2
        self.block_x = int(self.PYGAME_WIDTH/10)
        self.block_y = int(self.PYGAME_HEIGHT/8)

        self.multiplayer = multiplayer

        self.score = 0

        self.map = [[0, 0, 0, 0, 0, 0, 0, 1.1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0.1, 0, 0, 1.1, 0],
                    [0, 0, 0, 0, 0.2, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 4.2, 4.2, 1.1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        self.obstacle = obstacle()
        self.add_obstacle()

    def getScore(self):
        return str(self.score)

    def showCurrentElement(self, PYGAME_WIDTH, screen, tick, PYGAME_SPEED) :
        everyObject = []
        everyObject.append(sum(self.fixed.values(), []))
        everyObject.append(self.moving['playable']) # """sum(self.moving.values(), [])"""
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

    def rangeColumnOnScreen(self):
        firstColumn = (self.leftColumn - 1 if self.leftColumn != 0 else 0)
        return range(firstColumn, self.leftColumn + 11)

    def smartShow(self, screen) -> None:
        self.showAi(screen) # On oublie pas d'afficher toutes les IAs
        self.selectLeftColumn()
        for columnID in self.rangeColumnOnScreen():
            if columnID < len(self.elements): # Notre ID existe bien dans la liste elements qui enregistre tous nos objets
                for elem in self.elements[columnID]:
                    pixel_x = self.leftColumnPixel + (columnID - self.leftColumn)*self.block_x
                    if elem != None : elem.smartShowObject(screen, pixel_x, self.block_y)
            else : self.add_obstacle() # Puisque la map va se terminer, on ajoute un nouveau qui va mécaniquement ajouter de la longeur à la map


    def selectLeftColumn(self):
        if self.leftColumnPixel < -self.block_x:
            self.leftColumn += 1
            self.leftColumnPixel += self.block_x
            # On fait avancer le score si nécessaire
            if self.score < self.leftColumn : self.score = self.leftColumn
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
        everyMoving = self.moving['playable'] #sum(self.moving.values(), []) DEBUG pour retirer les ias

        for oneMoving in everyMoving:
            oneMoving.jumpExecute(currentTick, self, PYGAME_SPEED)

            isFalling = True

            if self.every_collision(oneMoving, 'b'):
                isFalling = False

            if not oneMoving.check_jump_without_num(currentTick):
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
        allPierceableOnScreen = []
        for columnID in self.rangeColumnOnScreen():
            if columnID < len(self.elements): # Notre ID existe bien dans la liste elements qui enregistre tous nos objets
                for elem in self.elements[columnID]:
                    if elem != None and elem.type == 'pierceable': allPierceableOnScreen.append(elem)

        for oneFixed in allPierceableOnScreen:
            if obj.check_collision(oneFixed):
                if (obj.get_start_y() + obj.get_size_y() - 10) <= (oneFixed.get_start_y()):
                    return True
        return False
    
    def everyFixed(self) -> list:
        everyFixed = []
        for goodIdColumn in self.rangeColumnOnScreen():
            if goodIdColumn < len(self.elements): # Notre ID existe bien dans la liste elements qui enregistre tous nos objets
                for elem in self.elements[goodIdColumn]:
                    if elem != None : everyFixed.append(elem)
        return everyFixed

    def every_collision (self, obj:object, direction:str) -> int:
        # everyFixed = sum(self.fixed.values(), [])

        everyFixed = self.everyFixed()
        for goodIdColumn in self.rangeColumnOnScreen():
            if goodIdColumn < len(self.elements): # Notre ID existe bien dans la liste elements qui enregistre tous nos objets
                for elem in self.elements[goodIdColumn]:
                    if elem != None : everyFixed.append(elem)

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
    

    def mapScroll(self, leftDirection:bool):
        PYGAME_SPEED = self.PYGAME_SPEED
        
        everyObject = []
        everyObject.append(self.everyFixed())
        everyObject.append(self.moving['playable'])#sum(self.moving.values(), []))
        everyObject = sum(everyObject, [])

        self.leftColumnPixel += (PYGAME_SPEED if leftDirection else -PYGAME_SPEED) # On déplace les objets fixes enregistrés dans les colonnes

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
        for column in self.obstacle.randomChoice(1):
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
        elif block == 3:
            return hitbox('pierceable', ref_x, ref_y+5/6, self.block_x, self.block_y/6, (214, 40, 40), ["img/platform.png"])
        elif block == 4:
            return hitbox('solid', ref_x, ref_y-0.5, self.block_x, self.block_y*1.5, (120, 120, 120), ["img/spike.png"])
        elif block == 4.1:
            return hitbox('solid', ref_x, ref_y, self.block_x, self.block_y, (148, 148, 148), ["img/rock.png"])
        elif block == 4.2:
            return hitbox('solid', (1/6)+ref_x, ref_y, (2/3)*self.block_x, self.block_y, (130, 130, 235), ["img/baril.png"])
        return None

    def movePlayer(self, playerNum:int, direction:str, tick:int=0):
        thisPlayer = self.moving['playable'][playerNum]

        if direction == 'd': # Le joueur a cliqué sur une touche de direction vers "la droite"
            if (not self.every_collision(thisPlayer, 'd')):
                if thisPlayer.get_start_x() + thisPlayer.get_size_x() >= 8*self.block_x:
                    if self.noPlayerOnOtherSide(True):
                        self.mapScroll(False)
                        thisPlayer.move_start_x(self.PYGAME_SPEED)
                else :
                    thisPlayer.move_start_x(self.PYGAME_SPEED)
                thisPlayer.set_lookDirection(0)

        elif direction == 'g': # Le joueur a cliqué sur une touche de direction vers "la gauche"
            if (not self.every_collision(thisPlayer, 'g')):
                if thisPlayer.get_start_x() <= self.block_x: 
                    if self.noPlayerOnOtherSide(False):
                        self.mapScroll(True)
                        thisPlayer.move_start_x(-self.PYGAME_SPEED)
                else :
                    thisPlayer.move_start_x(-self.PYGAME_SPEED)
                thisPlayer.set_lookDirection(1)

        elif direction == 'h': # Le joueur a cliqué sur une touche de direction vers "le haut"
            thisPlayer.create_jump(tick)

        elif direction == 'b': # Le joueur a cliqué sur une touche de direction vers "le bas"
            if self.goDown(thisPlayer):
                thisPlayer.move_start_y(self.PYGAME_SPEED)

    def noPlayerOnOtherSide(self, isLeftSideToCheck:bool):
        if isLeftSideToCheck:
            for player in self.moving['playable']:
                if player.get_start_x() <= self.block_x and player.alive(): return False
        else: # On vérifie alors si qqn reste sur le coté droit
            for player in self.moving['playable']:
                if player.get_start_x() + player.get_size_x() >= 8*self.block_x and player.alive(): return False

        return True # Si aucun joueur ne gène, on peut déplacer la map !
    
    def addAi(self, spawn_x_ref) -> None:
        self.moving['ai'].append(
            ai(self.block_x, hitbox(
                'ai',
                spawn_x_ref,
                5,
                self.block_x/2,
                self.block_y/2,
                (100, 240, 110),
                ["img/avocado.png"]
            ), spawn_x_ref)
        )

    def showAi(self, screen) -> None:
        for oneAi in self.moving["ai"]:
            oneAi.show(screen)

