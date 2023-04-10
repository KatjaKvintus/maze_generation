'''Module for randomized Kruskal's algorithm maze generation'''

import random


'''A list of all edges in the system'''
edges = []


class Cell:
    '''Module for handling cell related functions'''

    def __init__(self, x, y):
        '''x and y = coordinates in matrix
        open_edges = list of open edges to and from the cell'''
        self.x = x
        self.y = y
        self.open_edges = []
        self.set = set[(x, y)]

    def get_open_edges(self):
        return self.open_edges()


class Egde:
    '''Module for handling edge related functions'''

    def __init__(self, start_cell, end_cell):
        '''start_cell and end_cell define edge start and ending point
        is_open is True, if edge is open, and False, if not. At start
        every edge is closed.'''
        self.start_cell = start_cell
        self.end_cell = end_cell
        self.is_open = False


def open_edge(edge):
    '''Marks and edge open and adds it to both start and end cells
    open edges list'''
    edge.is_open = True
    (edge.start_cell).open_edges.append(edge)
    (edge.end_cell).open_edges.append(edge)


def add_edge(start, end):
    if start != end:
        edges.append(Egde(start, end))
        edges.append(Egde(end, start))



def create_kruskal_maze(size):
    '''Create a maze of required size. In the beginning every cell has walls around it.
    The list of 4 characters in each cell tells its wall situation.  A wall is marked
    by '1', a lack of wall is marked by '0'. At the beginning all walls are up so every 
    cell contains a list [1, 1, 1, 1]. The cell keeps track of its walls in this order: 
    left, top, right, bottom. '''

    '''A 2D list to keep track of matrix cells and walls.'''
    matrix = []

    for x in range(size):
        row = []
        for y in range(size):
            row.append(Cell(x, y))
        matrix.append(row)


    '''Adding edges to list'''
    for x in range(size):
        for y in range (size):

            start_cell = matrix[x][y]

            if x != 0:
                end_cell = matrix[x - 1][y]
                add_edge(start_cell, end_cell)

            if x != size -1:
                end_cell = matrix[x + 1][y]
                add_edge(start_cell, end_cell)

            if y != 0:
                end_cell = matrix[x][y - 1]
                add_edge(start_cell, end_cell)

            if y != size - 1:
                end_cell = matrix[x][y + 1]
                add_edge(start_cell, end_cell)

    random.shuffle(edges)

    '''Creating sets - at the begingnning every cell is in their own set'''
    
    for x in range(size):
        for y in range(size):
            matrix[x][y].set = set([(x, y)])

    '''Merging sets by removing walls one by one until there is only one set
    containing all cells = labyrinth'''
    i = 0

    while i < len(edges):
        cell_1 = edges[i].start_cell
        cell_2 = edges[i].end_cell

        if cell_1.set != cell_2.set:

            '''Open the edge both ways'''
            open_edge(edges[i])
            edges[i].is_open = True

            '''Transfer cell_2 set cells to cell_1 set'''
            cell_1.set |= cell_2.set

            for item in cell_2.set:
                matrix[item[0]][item[1]].set = cell_1.set

        i += 1

    return matrix


def print_kruskal_maze(maze):
    '''Provides image of the maze'''

    




# TESTIKOODIA

sokkelo = create_kruskal_maze(3)

print()