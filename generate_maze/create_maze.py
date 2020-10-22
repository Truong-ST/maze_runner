from tkinter import *
from prim_algorithm import PrimAlgorithm
import numpy as np
import time
import csv

w = 1000
h = 1000

tk = Tk()
tk.title('maze')
canvas = Canvas(tk, width=w, height=h)
tk.resizable(0, 0)
canvas.pack()

block = 20
margin = 20


def draw_map(size):
    for row in range(size[0]+2):
        for col in range(size[1]+2):
            if row == 0 or row == size[0]+1 or col == 0 or col == size[1]+1:
                canvas.create_rectangle(col * block +margin, row * block +margin, col * block +margin+block,
                                    row * block +margin+block, fill='black')                
                 
            canvas.create_rectangle(col * block +margin+int(block/2), row * block +margin+int(block/2), col * block +margin+2+int(block/2),
                                    row * block +margin+2+int(block/2), fill='black')
            
            
def create_point(position, size, color):
    canvas.create_rectangle(position[0], position[1], position[0]+size, position[1]+size, fill=color)
    
    
def increase_coordinate(pos, bias):
    return [pos[0]+bias, pos[1]+bias]


def scale_coordinate(list_coordinate, ratio, bias):
    scaled_list = []

    for coord in list_coordinate:
        tmp = [0, 0]
        tmp[0] = coord[1]*ratio + bias
        tmp[1] = coord[0]*ratio + bias
        scaled_list.append(tmp)

    return scaled_list


size = [41, 41]
a = PrimAlgorithm(size, [0, 0])
map_maze = a.prim()


# ------------------- Draw -------------------------

draw_map(size)

# set topographic
topographic = []
for i in range(size[0]):
    for j in range(size[1]):
        if map_maze[i][j] == 2:
            topographic.append(increase_coordinate([i, j], 1))

    
# draw wall
real_map = scale_coordinate(topographic, block, margin)
for pos in real_map:
    create_point(pos, block, 'blue')

tk.update()


tk.mainloop()


# file = open('map.csv', 'r')
# reader = csv.reader(file)
# print(reader)