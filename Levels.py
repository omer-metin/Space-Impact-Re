import numpy as np


display_w=800
display_h=500


class Explosion:

    def __init__(self, expx, expy):
        self.expx=expx
        self.expy=expy
        self.idx=0

# # # class Bomb:
    
# # #     def __init__(self, x, y):
# # #         self.x=x
# # #         self.y=y
# # #         self.y_move=0
# # #         self.yspeed=0

class Enemy:
    '''enemies:
        0:fireball
        1:rocket
        2:plane:
        3:enemyship
        4:level1boss'''
    def __init__(self, x, y, enemy_type, speed, fire_status, y_move, hp):
        self.x = x
        self.y = y
        self.enemy_type = enemy_type
        self.speed = speed
        self.yspeed = 4 if y_move else 0
        self.spawn = display_w#*0.9
        self.fire_status = fire_status
        self.hp = hp
        self.y_move = y_move
        self.fire_points = np.random.randint(200, display_w, size=3) if enemy_type else []
        if self.enemy_type in [0,1,3]:
            self.height = 25
        elif self.enemy_type in [2]:
            self.height = 35
        if self.enemy_type in [0,1]:
            self.width = 50
        elif self.enemy_type in [2]:
            self.width = 30
        elif self.enemy_type in [3]:
            self.width = 45


class Boss(Enemy):
    
    def __init__(self, x, y, enemy_type, speed, fire_status, y_move, hp):
        super().__init__(x, y, enemy_type, speed, fire_status, y_move, hp)
        
        self.yspeed=0
        if self.enemy_type == 4:
            self.height=120
            self.width=100


level_1=[
    Enemy(-200, 0, 0, 0, False, False, 1),                                 #0
    Enemy(display_w+200, display_h*0.2, 0, -4, False, False, 1), #1
    Enemy(display_w+80,  display_h*0.2, 0, -4, False, False, 1), #2
    Enemy(display_w+80,  display_h*0.2, 0, -4, False, False, 1), #3
    Enemy(display_w+280, display_h*0.4, 0, -4, False, False, 1), #4
    Enemy(display_w+80,  display_h*0.4, 0, -4, False, False, 1), #5
    Enemy(display_w+280, display_h*0.4, 0, -3, False, False, 1), #6
    Enemy(display_w+80,  display_h*0.4, 0, -3, False, False, 1), #7
    Enemy(display_w+80,  display_h*0.6, 0, -5, False, False, 1), #8
    Enemy(display_w+80,  display_h*0.6, 0, -5, False, False, 1), #9
    Enemy(display_w+80,  display_h*0.6, 0, -5, False, False, 1), #10
    Enemy(display_w+80,  display_h*0.2, 0, -5, False, False, 4), #11
    Enemy(display_w+80,  display_h*0.2, 0, -5, False, False, 4), #12
    Enemy(display_w+280, display_h*0.2, 2, -2, False, True,  1), #1
    Enemy(display_w+80,  display_h*0.4, 2, -2, False, True,  1), #2
    Enemy(display_w+80,  display_h*0.2, 2, -2, False, True,  1), #3
    Enemy(display_w+80,  display_h*0.4, 2, -2, False, True,  1), #4
    Enemy(display_w+80,  display_h*0.2, 2, -2, False, True,  1), #5
    Enemy(display_w+80,  display_h*0.4, 2, -2, False, True,  1), #6
    Enemy(display_w+80,  display_h*0.2, 2, -2, False, True,  1), #7
    Enemy(display_w+80,  display_h*0.4, 2, -2, False, True,  1), #8
    Enemy(display_w+280, display_h*0.6, 1, -6, False, False, 1), #1
    Enemy(display_w+280, display_h*0.2, 1, -5, False, False, 1), #2
    Enemy(display_w+80,  display_h*0.2, 1, -5, False, False, 1), #3
    Enemy(display_w+180, display_h*0.4, 1, -5, True,  True,  1), #4
    Enemy(display_w+80,  display_h*0.4, 1, -5, True,  True,  1), #5
    Enemy(display_w+80,  display_h*0.4, 1, -5, True,  True,  1), #6
    Enemy(display_w+80,  display_h*0.4, 1, -5, True,  True,  1), #7
    Enemy(display_w+80,  display_h*0.4, 1, -5, True,  True,  1), #8
    Enemy(display_w+80,  display_h*0.2, 1, -5, True,  True,  1), #9
    Enemy(display_w+80,  display_h*0.2, 1, -5, True,  True,  1), #10
    Enemy(display_w+80,  display_h*0.2, 1, -5, True,  True,  1), #11
    Enemy(display_w+80,  display_h*0.2, 1, -5, True,  True,  1), #12
    Enemy(display_w+280, display_h*0.15,3, -6, False, False, 2), #1
    Enemy(display_w+80,  display_h*0.15,3, -3, False, False, 2), #2
    Enemy(display_w+80,  display_h*0.2, 3, -3, False, False, 2), #3
    Enemy(display_w+80,  display_h*0.7, 3, -5, False, False, 2), #4
    Boss (display_w+180, display_h*0.2, 4, -3, True,  True, 20), #B*
]

