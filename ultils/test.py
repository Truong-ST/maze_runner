import numpy as np
# Python program to
# demonstrate implementation of
# queue using queue module
 
class I:
    def __init__(self):
        self.fitness = np.random.randint(0,100);
    
class P:
    def __init__(self):
        self.pops = []
        self.i()
    
    def i(self):
        for i in range(5):
            self.pops.append(I())
            
print("--------")      
p = P()
for i in p.pops:
    print(i)
    print(i.fitness)
p.pops.sort(key=lambda x: x.fitness)
print("--------")
for i in p.pops:
    print(i)
    print(i.fitness)

