import os
import numpy as np
import pygame
import Levels

# os.chdir("Space_impact")

pygame.init()

display_w=800
display_h=500
FPS=30
ship_speed=round(150/FPS)

def_font = pygame.font.Font(None, 35) 


black, green=(16,16,16), (145,251,150)

environments = {"black":os.listdir("black"), "green":os.listdir("green")}
bg_colors = {"black":(16,16,16), "green":(145,251,150)}

env = "black"

bg_color = bg_colors[env]
obj_color = green if env=="black" else black
sources=[os.path.join(env, environments[env][i]) for i in range(len(environments[env]))]
sources.sort()

gameDisplay = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("Space Impact")

clock = pygame.time.Clock()
#----------------------------------------------Levels-----------------------------------------------------#
level1=Levels.level_1
#--------------------------------------------Image Loads--------------------------------------------------#
ship_img      = pygame.image.load(sources[0])
live_img      = pygame.image.load(sources[1])
bomb_img      = pygame.image.load(sources[2])
laser_img     = pygame.image.load(sources[3])
mega_img      = pygame.image.load(sources[4])
fireball_img  = [pygame.image.load(sources[5]),  pygame.image.load(sources[6])]
rocket_img    = [pygame.image.load(sources[7]),  pygame.image.load(sources[8])]
plane_img     = [pygame.image.load(sources[9]),  pygame.image.load(sources[10])]
explosion_img = [pygame.image.load(sources[11]), pygame.image.load(sources[12])]
collided_ship = [pygame.image.load(sources[13]), pygame.image.load(sources[14])]
enemyship_img = pygame.image.load(sources[15])
level1Boss_img= [pygame.image.load(sources[16]), pygame.image.load(sources[17])]

#--------------------------------------------Functions----------------------------------------------------#
def ship(x,y): # 50x35 px 1 square=5 px
    gameDisplay.blit(ship_img,(x,y))

def col_ship(x, y, i):
    gameDisplay.blit(collided_ship[i], (x,y))

def fireball(i,enemy):
    gameDisplay.blit(fireball_img[i], (enemy.x,enemy.y))
    return enemy.x+enemy.speed

def rocket(i,enemy):
    gameDisplay.blit(rocket_img[i], (enemy.x,enemy.y))
    return enemy.x+enemy.speed

def plane(i,enemy):
    gameDisplay.blit(plane_img[i], (enemy.x,enemy.y))
    return enemy.x+enemy.speed

def enemyship(i,enemy):
    gameDisplay.blit(enemyship_img, (enemy.x,enemy.y))
    return enemy.x+enemy.speed

def boss(i,enemy):
    gameDisplay.blit(level1Boss_img[i], (enemy.x,enemy.y))
    if enemy.x < display_w*0.95-enemy.width:
        if enemy.yspeed==0:
            enemy.yspeed=-enemy.speed
        return enemy.x
    return enemy.x+enemy.speed
    

enemy_funcs=[fireball, rocket, plane, enemyship, boss]

def show_point(point):
    text = def_font.render("%.5d" %point, True, obj_color)
    gameDisplay.blit(text, (display_w*0.90,display_h*0.01))

def show_live(live):
    for i in range(live):
        gameDisplay.blit(live_img,(i*0.038*display_w+display_w*0.01,display_h*0.01))

def show_gun(gun, count):
    text = def_font.render("%.2d" %count, True, obj_color)
    gameDisplay.blit(gun, (display_w*0.46, display_h*0.01))
    gameDisplay.blit(text, (display_w*0.5, display_h*0.01))

def fire_ammo(ammox, ammoy): 
    pygame.draw.rect(gameDisplay, obj_color, [ammox, ammoy, 10, 5])

# # # def fire_bomb(enemies):
# # #     for enemy in enemies:
# # #         pass

# # # def fire_laser(enemies):
# # #     pass

# # # def fire_clear(enemies):
# # #     pass

# # # guns = [fire_bomb, fire_laser, fire_clear]

def explosion(expx, expy, i):
    gameDisplay.blit(explosion_img[i], (expx, expy))
    return i+1 if i<3 else 0

def ship_collision(shipx, shipy, enemies, enemy_ammos):
    for enemy in enemies[1:]:
        if enemy.x < shipx+50 and enemy.x+enemy.width > shipx:
            if enemy.y < shipy+35 and enemy.y+enemy.height > shipy:
                return True
    return False


#--------------------------------------------Game Loop----------------------------------------------------#

def gameloop():

    x, y = display_w * 0.07, display_h * 0.43
    x_change,y_change=0,0
    time_counter=0
    ship_status=0
    loop_idx=0
    
    explosions=[]
    live = 3
    point = 0
    gun, gun_count, gun_type = bomb_img, 3, 0
    ammos=[]
    enemy_ammos=[]

    gameExit = False

    while not gameExit and live>0:
        gameDisplay.fill(bg_color)
        
        loop_idx = (loop_idx + 1) % int(FPS/3)
        gif_idx=loop_idx // int((FPS/6))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit=True
        
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_w]:
                    y_change = -ship_speed 
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    y_change = ship_speed
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    x_change = -ship_speed
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    x_change = ship_speed
                if event.key == pygame.K_SPACE:
                    ammos.append([int(x+50),int(y+15)])
                # # # if event.key == pygame.K_q:
                # # #     if gun_type==0:
                # # #         pass
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_w, pygame.K_s):
                    y_change = 0
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d):
                    x_change = 0

        

        if ship_collision(x, y, level1, []) and ship_status == 0:
            ship_status = 1
            exp_x, exp_y=x, y
            x, y = display_w * 0.07, display_h * 0.43
            time_counter = pygame.time.get_ticks()
            live-=1
        

        for enemy in level1:    # Shooting enemy
            for ammo in ammos:
                if ammo[0]+10 > enemy.x and ammo[0] < enemy.x+enemy.width:
                    if ammo[1]+5 > enemy.y and ammo[1] < enemy.y+enemy.height and ammo[0]<display_w-5:
                        ammos.remove(ammo)
                        enemy.hp-=1
                        point+=5
                        if enemy.hp<=0:
                            level1.remove(enemy)
                            point+=5
                            explosions.append(Levels.Explosion(enemy.x,enemy.y))

        x+=x_change if x+x_change>display_w * 0.04 and x+x_change<display_w * 0.9 else 0
        y+=y_change if y+y_change>display_h * 0.08 and y+y_change<display_h * 0.9 else 0
        for ammo in ammos:
            fire_ammo(ammo[0], ammo[1])
            ammo[0]+=ship_speed*1.4
            if ammo[0]>1000: ammos.remove(ammo)
        for enemy_ammo in enemy_ammos:
            fire_ammo(enemy_ammo[0], enemy_ammo[1])
            enemy_ammo[0]-=ship_speed*1.4
            if enemy_ammo[0]<-100: enemy_ammos.remove(enemy_ammo)
        for exp in explosions:
            explosion(exp.expx, exp.expy, exp.idx//4)
            exp.idx+=1
            if exp.idx == 8:explosions.remove(exp)
        for idx_enemy, enemy in enumerate(level1):
            if level1[idx_enemy-1].x<enemy.spawn and enemy.x>-100 and enemy.hp>0:
                enemy.x = enemy_funcs[enemy.enemy_type](gif_idx, enemy)
            if enemy.y_move and enemy.x < display_w:
                if not (enemy.y < display_h*0.65 and enemy.y > display_h*0.15) and enemy.y > display_h*0.5:
                    enemy.yspeed=enemy.speed
                elif not (enemy.y < display_h*0.65 and enemy.y > display_h*0.15) and enemy.y < display_h*0.5:
                    enemy.yspeed=-enemy.speed
                enemy.y += enemy.yspeed
                


        if ship_status == 0:
            ship(x,y)
        elif ship_status == 1:
            explosion(exp_x, exp_y, gif_idx)
            if pygame.time.get_ticks() > time_counter+300:
                ship_status = 2
        elif ship_status == 2:
            col_ship(x-10, y-10, gif_idx)
            if pygame.time.get_ticks() > time_counter+2700:
                ship_status = 0


        show_live(live)
        show_point(point)
        show_gun(gun, gun_count)

        

        pygame.display.update()
        clock.tick(FPS)
 

gameloop()
pygame.quit()
quit()
