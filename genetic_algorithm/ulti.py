import csv
import numpy as np


def get_topograph(fileName):
    map_maze = []
    file = open(fileName, 'r')
    reader = csv.reader(file)
    for row in reader:
        tmp = list(map(int, row))
        map_maze.append(tmp)
    
    return map_maze


def get_wall(map_maze):
    walls = []
    for i in range(len(map_maze)):
        for j in range(len(map_maze[0])):
            if map_maze[i][j] == 2:
                walls.append(np.array([i, j]))
                
    return walls


def scale_coordinate(list_coordinate, ratio, bias):
    scaled_list = []

    for coord in list_coordinate:
        # tmp = [0, 0]
        # tmp[0] = coord[1]*ratio + bias
        # tmp[1] = coord[0]*ratio + bias
        tmp = coord*ratio + bias
        scaled_list.append(np.array(tmp))

    return scaled_list


def coord_to_pos(coord, ratio, bias):
    pos = ((coord-bias) / ratio).astype(int)
    return pos
    # x = (coord[1]-bias) / ratio
    # y = (coord[0]-bias) / ratio
    # return np.array([x, y])
    