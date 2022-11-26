import pygame
import random
import time

robot_size = 10
step = 0.5
map_x = 500
map_y = 500 
pygame.init()
dis=pygame.display.set_mode((map_x,map_y))

background = (0, 0, 0)

robot_color=(255,0,0) 

x = map_x/2 # start x
y = map_y/2 # start y
robot_size = 10
step = 0.5


directions = ['up','down','left','right']
direc = random.choice(directions)

while True:
    #direc = random.choice(directions)
    if 	 direc == 'up'   :
        #next_y += -0.1
        if (y  - step - robot_size) <= 0:
            direc = random.choice(directions)
            continue
        else:
            y -= step
    elif direc == 'down' :
        #next_y += 0.1
        if (y  + step + robot_size) >= map_y:
            direc = random.choice(directions)
            continue
        else:
            y += step
    elif direc == 'left' :
        #next_x += -0.1
        if (x  - step - robot_size) <= 0:
            direc = random.choice(directions)
            continue
        else:
            x -= step
    elif direc == 'right':
        #next_x += 0.1
        if (x  + step + robot_size) >= map_x:
            direc = random.choice(directions)
            continue
        else:
            x += step
    
    
    dis.fill(background)
    pygame.draw.circle(dis, robot_color, (x,y), robot_size) 
    pygame.display.update()
    time.sleep(0.005)
    #clock.tick(4000)
pygame.quit()
quit()

