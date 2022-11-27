import pygame
import random
import time

step = 1
robot_size = 10
map_x = 500
map_y = 500 
x = map_x/2 # start x
y = map_y/2 # start y
background = (0, 0, 0)
robot_color=(255,0,0)
next_x = 0
next_y = 0

array = []
ind_x = 0
ind_y = 0

pygame.init()
dis=pygame.display.set_mode((map_x,map_y))

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
        temp_x = round(((inp - 90.00) * (step - 0.00) / (180.00 - 90.0) + 0.00),3)
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

def print_map():
    dis.fill(background)
    pygame.draw.circle(dis, robot_color, (x,y), robot_size)
    for i in range(len(array)):
        pygame.draw.rect(dis,(255,255,255),[array[i][0],array[i][1],10,10])
    
    pygame.display.update()

def valid_move():
    if ((y + next_y - robot_size) <= 0) or ((y + next_y + robot_size) >= map_y) or ((x + next_x - robot_size) <= 0.0) or ((x + next_x + robot_size) >= map_x):
        return False
    return True

def generate_trash():
    for i in range(200):    
        ind_x = random.uniform(0,map_x-10)
        ind_y = random.uniform(0,map_y-10)
        if [ind_x,ind_y] not in array:
            array.append([ind_x,ind_y])

#directions = ['up','down','left','right']
#x,y = _map(random.randint(0,360))
next_x, next_y = _map(random.randint(0,359))
generate_trash()
score = 0
while True:
    
    if not valid_move() :
        next_x,next_y = _map(random.randint(0,360))
        continue
    else:
        x += next_x
        y += next_y
    
    if [x,y] in array:
        array.remove[x,y]
        score += 1
        print(score)
     
    for i in range(len(array)):
        if (x-robot_size <= array[i][0] <= x + robot_size) and (y-robot_size <= array[i][1] <= y + robot_size):
            score += 1
            print(score)
            array.pop(i)
            break
            
    print_map()
    time.sleep(0.005)
    
pygame.quit()
quit()