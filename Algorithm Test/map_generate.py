import json
import random
import pygame

#pygame.init()

map_x = 500
map_y = 500

#dis=pygame.display.set_mode((map_x,map_y))


dictionary = {
    
  "map1": [
    {
      "shape": "rectangle",
      "position x": 0,
      "position y": 0,
      "size x": 200,
      "size y": 200
    }
  ],
  
  "map2": [
    {
      "shape": "rectangle",
      "position x": 0,
      "position y": 0,
      "size x": 200,
      "size y": 200
    },
    {
      "shape": "rectangle",
      "position x": 300,
      "position y": 300,
      "size x": 200,
      "size y": 200
    }    
  ]
}


json_object = json.dumps(dictionary)
print(json_object)
'''
json_object = json.dumps(dictionary2)
with open("map1.json", "w") as outfile:
    outfile.write(json_object)
    
    

background = (0, 0, 0)

dis.fill(background)

#pygame.draw.circle(dis, (255,255,255), (obj_array[i].pos_x,obj_array[i].pos_x), obj_array[i].size_x)
#pygame.draw.rect(dis,(255,255,255),[obj_array[i].pos_x,obj_array[i].pos_x,obj_array[i].size_x,obj_array[i].size_y])

pygame.draw.rect(dis,(255,255,255),[300,300,200,200])

pygame.display.update()
'''