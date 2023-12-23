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
    
    def gravity(self, currentTick:int):
        everyMoving = sum(self.moving.values(), [])
        everyFixed = sum(self.fixed.values(), [])

        for oneMoving in everyMoving:
            isFalling = True
            for oneFixed in everyFixed:
                if oneMoving.check_collision(oneFixed):
                    isFalling = False

            if isFalling:
                oneMoving.move_start_y(2)
            elif oneMoving.check_jump_without_num(currentTick):
                oneMoving.reset_num_jump()
