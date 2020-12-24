from individual import Individual


class Popuation:
    def __init__(self, start, amount):
        self.amount = amount
        self.individuals = []
        self.fitness_test = 0
        self.start = start
    
    def initialize_population(self):
        for i in range(self.amount):
            self.individuals.append(Individual(self.start))
        print('generate')
    
    
    def calculate_fitness(self, goal):
        for individual in self.individuals:
            individual.calculate_fitness(goal)
    
        
    def get_fitnessest(self):
        pass
        