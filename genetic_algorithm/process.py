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
        self.fittest = 0
        self.generation = 0
        self.survival = amount // 3
        
        self.overfit = []


    def selection(self):
        self.pops.individuals.sort(key=lambda x: x.fitness)
        del self.pops.individuals[self.survival:]
        
        # renew
        for indi in self.pops.individuals:
            indi.position = self.start.astype(float)
            indi.phi = 0
            
        self.fittest = self.pops.individuals[0].fitness
        

    def crossover(self, ratio):
        # crossover_point = np.random.randint(50, 100)
        crossover_point = ratio % self.amount
        new = 20
        
        son = individual.Individual(self.start)
        son.gene_phi = self.pops.individuals[0].gene_phi.copy()[:crossover_point] + self.pops.individuals[1].gene_phi.copy()[crossover_point:]
        daughter = individual.Individual(self.start)
        daughter.genes = self.pops.individuals[1].gene_phi.copy()[:crossover_point] + self.pops.individuals[0].gene_phi.copy()[crossover_point:]
        
        self.pops.individuals.append(son)
        self.pops.individuals.append(daughter)
        
        
        for i in range((self.amount-self.survival)-new-2):
            pos_dad = np.random.randint(0, self.survival)
            pos_mom = np.random.randint(0, self.survival)

            offspring = individual.Individual(self.start)
            offspring.gene_phi = self.pops.individuals[pos_dad].gene_phi.copy()[:crossover_point] + self.pops.individuals[pos_mom].gene_phi.copy()[crossover_point:]
            
            self.pops.individuals.append(offspring)
            
        for i in range(new):
            self.pops.individuals.append(individual.Individual(self.start))

    def mutation(self, ratio):
        number_genes = 50
        
        for i in range(ratio):
            index = np.random.randint(5, self.amount)
            indi = self.pops.individuals[index]
            
            for j in range(number_genes):
                indi.gene_phi[np.random.randint(0, 100)] -= 0
                

    def relate_offspring(self):
        pass
    
    
    def optimal_gene(self):
        pass
    
    
    def check_overfit(self):
        pass
