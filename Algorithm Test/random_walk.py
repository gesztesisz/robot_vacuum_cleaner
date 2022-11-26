import pygame
import random
import time

step = 1
robot_size = 10
map_x = 500
map_y = 500 

def _map(inp):
    if inp == 0 or inp == 360:
        return step,0.0
    elif inp == 90:
        return 0.0,-step
    elif inp == 180:
        return -step,0.0
    elif inp == 270:
        return 0.0,step
    elif inp == 45:
        return step/2,-step/2
    elif inp == 135:
        return -step/2,-step/2
    elif inp == 225:
        return -step/2,step/2
    elif inp == 315:
        return step/2,step/2
    
    if inp > 0 and inp < 90:
        temp_x = round(((inp - 0.00) * (step - 0.00) / (90.00 - 0.0) + 0.00),3)
        temp_y = round(step - temp_x,3)
        if inp < 45:
            temp_x,temp_y = temp_y,temp_x
            return temp_x,-temp_y
        elif inp > 45:
            temp_x,temp_y = temp_y,temp_x
            return temp_x,-temp_y
    elif inp > 90 and inp < 180:
        temp_x = round(((inp - 90.00) * (1.00 - 0.00) / (180.00 - 90.0) + 0.00),3)
        temp_y = round(step - temp_x,3)
        if inp < 135:
            return -temp_x,-temp_y
        elif inp > 135:
            return -temp_x,-temp_y
    elif inp > 180 and inp < 270:
        temp_x = round(((inp - 180.00) * (step - 0.00) / (270.00 - 180.0) + 0.00),3)
        temp_y = round(step - temp_x,3)
        if inp < 225:
            temp_x,temp_y = temp_y,temp_x
            return -temp_x,temp_y
        elif inp > 225:
            temp_x,temp_y = temp_y,temp_x
            return -temp_x,temp_y
    elif inp > 270 and inp < 360:
        temp_x = round(((inp - 270.00) * (step - 0.00) / (360.00 - 270.0) + 0.00),3)
        temp_y = round(1.00 - temp_x,3)
        if inp < 315:
            return temp_x,temp_y
        elif inp > 315:
            return temp_x,temp_y

pygame.init()
dis=pygame.display.set_mode((map_x,map_y))

background = (0, 0, 0)

robot_color=(255,0,0) 

x = map_x/2 # start x
y = map_y/2 # start y

#directions = ['up','down','left','right']
#x,y = _map(random.randint(0,360))
next_x, next_y = _map(random.randint(0,359))

while True:
    
    if ((y + next_y - robot_size) <= 0) or ((y + next_y + robot_size) >= map_y) or ((x + next_x - robot_size) <= 0.0) or ((x + next_x + robot_size) >= map_x):
        next_x,next_y = _map(random.randint(0,360))
        continue
    else:
        x += next_x
        y += next_y
    
    dis.fill(background)
    pygame.draw.circle(dis, robot_color, (x,y), robot_size) 
    pygame.display.update()
    #print('x: ',x, 'y: ',y)
    time.sleep(0.005)
    
pygame.quit()
quit()


