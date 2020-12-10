import numpy as np
import random
import math
import csv


class PrimAlgorithm:
    def __init__(self, size, start):
        self.row, self.column = size
        self.start = start
        self.mark = np.full([self.row, self.column], 2)
        self.mark[start[0]][start[1]] = 0 # 1 : checked, 2: wall
        
        self.came_from = []
        for i in range(self.row):
            tmp = []
            for j in range(self.column):
                tmp.append([])
            self.came_from.append(tmp)
        self.came_from[start[0]][start[1]] = start
        
    
    def list_neighbor(self, current):
        """
        :return: list of around(8) current
        """
        list_neighbor = []
        phi = 0

        for i in range(4):
            delta_col = round(math.cos(phi))
            delta_row = round(math.sin(phi))

            next_col = current[1] + 2 * delta_col
            next_row = current[0] + 2 * delta_row

            if (0 <= next_col < self.column) and (0 <= next_row < self.row):
                list_neighbor.append([next_row, next_col])

            phi += math.pi / 2

        return list_neighbor
    
    
    def connect(self, node):
        pre_node = self.came_from[node[0]][node[1]]
        
        wall_0 = int((pre_node[0]+node[0]) / 2)
        wall_1 = int((pre_node[1]+node[1]) / 2)
        self.mark[wall_0][wall_1] = 0
    
    
    def prim(self):
        open_set = [self.start]
        
        while open_set:
            current = open_set.pop(random.randint(0, len(open_set)-1))
            self.connect(current)
            
            for neighbor in self.list_neighbor(current):
                a , b = neighbor      
                
                if self.mark[a][b] == 2:                    
                    open_set.append(neighbor)
                    self.came_from[a][b] = current
                    
                    self.mark[a][b] = 0
        
        print('done')
        return self.mark
                    
                    
if __name__ == "__main__":
    size = [37, 37]
    a = PrimAlgorithm(size, [0, 0])
    map_maze = a.prim()
    
    file = open('maze.csv', 'w', newline='')
    writer = csv.writer(file)
    writer.writerows(list(map_maze))
    file.close()