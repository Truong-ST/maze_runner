import numpy as np
import math


class Individual:
    def __init__(self, start):
        self.fitness = 0
        self.gene_length = 200
        self.gene_phi = []
        self.gene_time = []
        self.initialize_individual()
        self.start = start
        self.position = self.start.astype(float)
        
       
    def initialize_individual(self):
        pi2 = math.pi * 2
        for i in range(self.gene_length):
            self.gene_phi.append(np.random.uniform(0, pi2))
            self.gene_time.append(np.random.randint(2, 5))
            
            
    def move(self, phi, v, t):
        x, y = t*v * math.cos(phi), t*v * math.sin(phi)
        self.position += np.array([x, y])
        # return self.position
        return np.array([x, y])
        
    
    # def calculate_fitness(self, goal):
    #     pos = self.start
    #     self.position = self.start.astype(float)
    #     v = 6
    #     for i in range(self.gene_length):
    #         phi = self.gene_phi[i]
    #         t = self.gene_time[i]
    #         pos = self.move(phi, v, t)
            
    #     self.fitness = np.linalg.norm(goal-pos)
    def calculate_fitness(self, goal):
        self.fitness = np.linalg.norm(goal-self.position)
            
    
