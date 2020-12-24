import numpy as np
import math


class Individual:
    def __init__(self, start):
        self.fitness = 0
        self.moved = 0
        self.theta = 0
        self.phi = math.pi / 3
        
        self.gene_length = 250
        self.gene_phi = []
        self.gene_time = [1]
        self.initialize_individual()
        self.start = start
        self.position = self.start.astype(float)
        self.pi2 = math.pi * 2
        
       
    def initialize_individual(self):
        self.gene_phi.append(np.random.uniform(0, math.pi * 2))
        for i in range(self.gene_length-1):
            self.gene_phi.append(np.random.uniform(-self.phi, self.phi))
            self.gene_time.append(np.random.randint(2, 5))
            
            
    def move(self, theta, v, t):
        self.theta += theta
        x, y = t*v * math.cos(self.theta), t*v * math.sin(self.theta)
        self.position += np.array([x, y])
        
        return np.array([x, y])
        
    
    def calculate_fitness(self, goal):
        self.fitness = np.linalg.norm(goal-self.position) + self.moved / 10
            
    
