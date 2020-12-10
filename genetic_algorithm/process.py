import numpy as np
import time
import math
from tkinter import *
from population import Popuation
import individual
from ulti import *
from heuristic import distance_euclid


class Main:
    def __init__(self, start, amount):
        self.start = start
        self.amount = amount
        self.pops = Popuation(start, amount)
        self.pops.initialize_population()
        self.fittest = individual.Individual(start)
        self.generation = 0
        self.survival = amount // 2


    def selection(self):
        self.pops.individuals.sort(key=lambda x: x.fitness)
        del self.pops.individuals[self.survival:]
        # return self.pops.individuals[0:self.survival]
        

    def crossover(self, ratio):
        # crossover_point = np.random.randint(50, 100)
        crossover_point = ratio
        # m = self.survival // 2 
        new = 5
        
        for i in range(self.survival-new+1):
            pos_dad = np.random.randint(0, self.survival)
            pos_mom = np.random.randint(0, self.survival)
            # dad = self.pops.individuals[pos_dad]
            # mom = self.pops.individuals[pos_mom]
            
            son = individual.Individual(self.start)
            son.gene_phi = self.pops.individuals[pos_dad].gene_phi.copy()[:crossover_point] + self.pops.individuals[pos_mom].gene_phi.copy()[crossover_point:]
            # daughter = individual.Individual(self.start)
            # daughter.genes = mom.genes[:crossover_point] + dad.genes[crossover_point:]
            
            self.pops.individuals.append(son)
            # self.pops.individuals.append(daughter)
            
        for i in range(new):
            self.pops.individuals.append(individual.Individual(self.start))
            

    def mutation(self):
        amount = 10
        number_genes = 5
        
        for i in range(amount):
            index = np.random.randint(0, self.amount)
            gene_phi = self.pops.individuals[index].gene_phi.copy()
            
            for j in range(number_genes):
                gene_phi[np.random.randint(0, 100)] -= 0
                
            self.pops.individuals[index].gene_phi = gene_phi


    def relate_offspring(self):
        pass
    
    
    def renew(self):
        for indi in self.pops.individuals:
            indi.position = self.start.astype(float)


if __name__ == '__main__':
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
        
        
    start = np.array([100, 100])
    goal = np.array([600, 600])
    width = 900
    height = 900
    amount = 60
    length = 150
    
    root = Tk()
    root.title('illustration')
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    root.resizable(0, 0)

    topograph = get_topograph('maze.csv')
    walls = get_wall(topograph)
    real_wall = scale_coordinate(walls, 20, 10)
    
    main = Main(start, amount)
        
    canvas.create_rectangle(*start, *(start + 10), fill='red')
    canvas.create_rectangle(*goal, *(goal + 10), fill='red')
    for wall in real_wall:
        create_point(wall, 20, 'gray')
    
    count_generation = 0
    generation_count = canvas.create_text(width-20, 20, text='0')
    pop  = canvas.create_text(width-20, 40, text = '0')
    
    while count_generation < 150:
        canvas.itemconfigure(pop, text=str(len(main.pops.individuals)))
        v = 4
        
        check = []
        list_indi = []
        live = []
        for i in range(amount):
            check.append(False)
            live.append(1)
            list_indi.append(canvas.create_rectangle(*start, *(start + 4), fill='blue'))
            
        for i in range(0, length):
            for j in range(amount):
                phi = main.pops.individuals[j].gene_phi[i]
                t = main.pops.individuals[j].gene_time[i]
                
                if live[j] == 1:
                    # canvas.move(list_indi[j], t*v*math.cos(phi), t*v*math.sin(phi))
                    canvas.move(list_indi[j],*main.pops.individuals[j].move(phi, v, t))
                if list(coord_to_pos(main.pops.individuals[j].position, 20, 10)) in list(map(list, walls)) or check_outside(main.pops.individuals[j].position, [width, height]):
                    live[j] = 0
                    
            root.update() 
            # time.sleep(0.01)
            
        for i in range(amount):
            check[i] = check_come(main.pops.individuals[j].position, goal)
        if check_done(check):
            print('done')
            break
            
        canvas.itemconfigure(generation_count, text=str(count_generation))
        ratio = count_generation
        
        main.pops.calculate_fitness(goal)
        main.selection()
        main.crossover(ratio)
        main.mutation()
        
        for i in range(amount):
            canvas.delete(list_indi[i])
        
        time.sleep(0.05)
        count_generation += 1
    
    root.mainloop()    
    
    
