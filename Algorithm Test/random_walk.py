import pygame
import random
import time

class obstacle_obj:
    def __init__ (self,pos_x,pos_y,shape,size_x,size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.shape = shape
        self.size_x = size_x
        self.size_y = size_y
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
wait = 0.005
num_of_trash = 100
num_of_obstacle = 20

trash_array = []

obstacle_array = []
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
    for i in range(len(trash_array)):
        pygame.draw.rect(dis,(255,255,255),[trash_array[i][0],trash_array[i][1],10,10])
        
    for i in range(len(obstacle_array)):
        pygame.draw.rect(dis,(125,125,125),[obstacle_array[i][0],obstacle_array[i][1],10,10])
    pygame.display.update()

def its_wall():
    if ((y + next_y - robot_size) <= 0) or ((y + next_y + robot_size) >= map_y) or ((x + next_x - robot_size) <= 0.0) or ((x + next_x + robot_size) >= map_x):
        return True
    return False
'''
def its_obstacle():
    for i in range(len(obstacle_array)):
        if ((y + next_y - robot_size) <= obstacle_array[]) or ((y + next_y + robot_size) >= map_y) or ((x + next_x - robot_size) <= 0.0) or ((x + next_x + robot_size) >= map_x):
            return False
    return True
'''
def generate_trash():
    for i in range(num_of_trash):    
        ind_x = random.uniform(0,map_x-10)
        ind_y = random.uniform(0,map_y-10)
        if [ind_x,ind_y] not in trash_array:
            trash_array.append([ind_x,ind_y])

def collect_trash():
    for i in range(len(trash_array)):
        if (x-robot_size-2 <= trash_array[i][0] <= x + robot_size-2) and (y-robot_size-2 <= trash_array[i][1] <= y + robot_size-2):
            score += 1
            print(score)
            trash_array.pop(i)
            break



#directions = ['up','down','left','right']
#x,y = _map(random.randint(0,360))
next_x, next_y = _map(random.randint(0,359))
generate_trash()
generate_obstacle()
score = 0
while True:
    
    if its_wall() :
        next_x,next_y = _map(random.randint([90,-90]))
        time.sleep(wait)
        continue
    else:
        x += next_x
        y += next_y
    
    
    #collect_trash()
            
    print_map()
    time.sleep(wait)
    
pygame.quit()
quit()
