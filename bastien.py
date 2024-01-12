class reference:
    def __init__ (self):
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
    
    def add_moving_as(self, key:str, obj:object):
        self.moving[key].append(obj)
    def add_fixed_as(self, key:str, obj:object):
        self.fixed[key].append(obj)

    def get_moving_as(self, key:str):
        return self.moving[key]
    def get_fixed_as(self, key:str):
        return self.fixed[key]
    
    def gravity(self, currentTick:int, PYGAME_SPEED):
        everyMoving = sum(self.moving.values(), [])

        for oneMoving in everyMoving:
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
                    result = True
        
        if direction == 'g':
            for obstacle in listFixed:
                if (obstacle.get_start_x() + obstacle.get_size_x() - 10) <= (obj.get_start_x()):
                    result = True
        
        return result
    

    def mapScroll(self, leftDirection:bool, whichPlayer:object=None):
        everyObject = []
        everyObject.append(sum(self.fixed.values(), []))
        everyObject.append(sum(self.moving.values(), []))
        everyObject = sum(everyObject, [])

        for obj in everyObject:
            obj.


