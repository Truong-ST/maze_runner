from process import Main
import numpy as np
import time
import math
from tkinter import *
from tkinter import messagebox
from population import Popuation
import individual
from ulti import *


block = 20
margin = 10


def create_point(position, size, color):
        canvas.create_rectangle(*position, *(position + size), fill=color)


def check_outside(pos, width, height):
    if margin <= pos[0] <= width and margin <= pos[1] <= height:
        return False
    return True 

    
def check_come(pos1, pos2):
    if np.linalg.norm(pos1-pos2) < 20:
        return True
    return False


def check_done(list_check):
    count = 0 
    for i in range(len(list_check)):
        if list_check[i]:
            count += 1
            
    if count > len(list_check) / 5:
        return True
    return False
    
    
size = [41, 41]
# start = np.array([100, 100])
# goal = np.array([600, 600])
# goal = np.array([520, 680])
# goal = np.array([350, 520])
start = np.array([200, 100])
goal = np.array([350, 730])
width = size[0] * block + margin + 50
height = size[1] * block + margin + margin
w = width - 50
h = height - margin

num_generation = 250
amount = 100
v = 4
r = np.array([20, 20])

root = Tk()
root.title('illustration')
canvas = Canvas(root, width=width, height=height)
canvas.pack()
root.resizable(0, 0)

# read map
topograph = get_topograph('demo.csv')
walls = get_wall(topograph)
real_wall = scale_coordinate(walls, block, margin)

main = Main(start, amount)
length = main.pops.individuals[0].gene_length

# draw
canvas.create_rectangle(margin, margin, w, h, outline='black')
canvas.create_rectangle(*start, *(start + 10), fill='red')
canvas.create_oval(*(goal-r), *(goal+r), fill='red')
for wall in real_wall:
    create_point(wall, 20, 'gray')

count_generation = 0
generation_count = canvas.create_text(width-20, 20, text='0')
pop  = canvas.create_text(width-20, 40, text = '0')
over = 0

while count_generation < num_generation:
    canvas.itemconfigure(pop, text=str(len(main.pops.individuals)))
    
    check = []
    list_indi = []
    live = []
    for i in range(amount):
        check.append(False)
        live.append(1)
        list_indi.append(canvas.create_rectangle(*start, *(start + 4), fill='blue'))
        
    # count_live = 0
    for i in range(0, length):
        for j in range(amount):
            if live[j] == 1:
                indi = main.pops.individuals[j]
                phi = indi.gene_phi[i]
                t = indi.gene_time[i]
                # canvas.move(list_indi[j], t*v*math.cos(phi), t*v*math.sin(phi))
                canvas.move(list_indi[j], *indi.move(phi, v, t))
                
                position = indi.position
                pos = coord_to_pos(position, block, margin)
                
                if check_come(position, goal):
                    check[j] = True
                    live[j] = 0
                    indi.moved = i
                    indi.fitness = 0
                    
                if topograph[pos[0]][pos[1]] == 2:
                    live[j] = 0
                    indi.moved = i
                    # indi.fitness = 0
                else :    
                    if check_outside(position, w, h):
                        live[j] = 0
                        indi.moved = i
                        # indi.fitness = 0
                
        root.update() 
        # time.sleep(0.001)

    # print path
    if check_done(check):
        print(count_generation)
        for i in range(amount):
            if check[i]:
                pos = start
                indi = main.pops.individuals[i]
                phi = 0
                print(indi.moved)
                for i in range(indi.moved):
                    phi += indi.gene_phi[i]
                    t = indi.gene_time[i]
                    next_pos = pos + np.array([t*v*math.cos(phi), t*v*math.sin(phi)])
                    canvas.create_line(*pos, *next_pos)
                    pos = next_pos
                    
        messagebox.showinfo('Message', 'Find')
        break
        
    canvas.itemconfigure(generation_count, text=str(count_generation))
    point = count_generation * 10
    ratio_mutation = 12
    
    # main.pops.calculate_fitness(goal)
    for i in range(amount):
        if check[i]:
            continue
        main.pops.individuals[i].calculate_fitness(goal)
        
    main.selection()
    main.crossover(point)
    
    over = main.pops.individuals[5].moved
    # print(over)
    
    main.mutation(ratio_mutation, over)
    main.add_new()
    # print(main.fittest)
    for i in range(amount):
        canvas.delete(list_indi[i])
        
    time.sleep(0.05)
    count_generation += 1

for i in range(3):
    pos = start
    indi = main.pops.individuals[i]
    phi = 0
    print(indi.moved)
    for i in range(indi.moved):
        phi += indi.gene_phi[i]
        t = indi.gene_time[i]
        next_pos = pos + np.array([t*v*math.cos(phi), t*v*math.sin(phi)])
        canvas.create_line(*pos, *next_pos)
        pos = next_pos

root.mainloop()    
