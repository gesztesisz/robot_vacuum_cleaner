import pygame
import random
import time

robot_size = 10
map_x = 500
map_y = 500 
pygame.init()
dis=pygame.display.set_mode((map_x,map_y))

background = (0, 0, 0)

robot_color=(255,0,0) 

x = map_x/2 # start x
y = map_y/2 # start y

directions = ['up','down','left','right']


while True:
    direc = random.choice(directions)
    if 	 direc == 'up'   :
        y += -0.1
    elif direc == 'down' :
        y += 0.1
    elif direc == 'left' :
        x += -0.1
    elif direc == 'right':
        x += 0.1

    dis.fill(background)
    pygame.draw.circle(dis, robot_color, (x,y), robot_size) 
    pygame.display.update()
    time.sleep(0.005)
    #clock.tick(4000)
pygame.quit()
quit()

