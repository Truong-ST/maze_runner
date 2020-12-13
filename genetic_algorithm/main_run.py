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


def check_outside(pos, size):
    if 0 <= pos[0] <= size[0] and 0 <= pos[1] <= size[1]:
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
start = np.array([100, 100])
goal = np.array([600, 600])
num_generation = 200
width = 850
height = 850
amount = 100
length = 150
v = 4
r = np.array([20, 20])

root = Tk()
root.title('illustration')
canvas = Canvas(root, width=width, height=height)
canvas.pack()
# root.resizable(0, 0)

topograph = get_topograph('map.csv')
walls = get_wall(topograph)
real_wall = scale_coordinate(walls, block, margin)

main = Main(start, amount)
    
canvas.create_rectangle(*start, *(start + 10), fill='red')
canvas.create_oval(*(goal-r), *(goal+r), fill='red')
for wall in real_wall:
    create_point(wall, 20, 'gray')

count_generation = 0
generation_count = canvas.create_text(width-20, 20, text='0')
pop  = canvas.create_text(width-20, 40, text = '0')

while count_generation < num_generation:
    canvas.itemconfigure(pop, text=str(len(main.pops.individuals)))
    
    check = [False] * amount
    list_indi = []
    live = [1] * amount
    for i in range(amount):
        list_indi.append(canvas.create_rectangle(*start, *(start + 4), fill='blue'))
        
    # count_live = 0
    for i in range(0, length):
        for j in range(amount):
            phi = main.pops.individuals[j].gene_phi[i]
            t = main.pops.individuals[j].gene_time[i]
            
            if live[j] == 1:
                # canvas.move(list_indi[j], t*v*math.cos(phi), t*v*math.sin(phi))
                canvas.move(list_indi[j], *main.pops.individuals[j].move(phi, v, t))
            
            position = main.pops.individuals[j].position
            pos = coord_to_pos(position, block, margin)
            if check_come(position, goal):
                check[j] = True
                live[j] = 0
                
            if check_outside(position, [width, height]):
                live[j] = 0
            else :    
                if topograph[pos[0]][pos[1]] == 2:
                    live[j] = 0
                # count_live += 1
                
        # if count_live == amount:
        #     break
                
        root.update() 
        time.sleep(0.01)
        
    # for i in range(amount):
    #     check[i] = check_come(main.pops.individuals[j].position, goal)
    if check_done(check):
        print('done')
        messagebox.showinfo('Message', 'FIND')
        break
        
    canvas.itemconfigure(generation_count, text=str(count_generation))
    point = count_generation * 10
    ratio_mutation = 10
    
    main.pops.calculate_fitness(goal)
    main.selection()
    main.crossover(point)
    main.mutation(ratio_mutation)
    
    for i in range(amount):
        canvas.delete(list_indi[i])
    
    time.sleep(0.05)
    count_generation += 1

root.mainloop()    
