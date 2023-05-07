'''A Module for analyzing maze paths'''
from maze_generation import backtracker
    

def are_all_cells_reachable(matrix):
    '''Returns True if BFS can visits every cell in the maze
    that is modeled as a 2D array (like backtracker)'''

    size = len(matrix)

    # List to keep track of visited nodes.
    visited_cells = [[[False] for i in range(size)] for j in range(size)]

    queue = []

    start_x = 0
    start_y = 0

    return breadth_first_search(visited_cells, matrix, start_x, start_y, queue)


def breadth_first_search(visited_cells, matrix, x, y, queue):
    '''BFS algorithm, a helper mothed for are_all_cells_reachable().
    Returns True is all cells are visited during search.'''

    visited_cells[x][y] = [True]
    queue.append([x, y])

    # Continue as long as queue has cells to visit
    while len(queue) > 0:

        next_cell = queue.pop(0) 

        neighbors = find_available_neighbour(next_cell[0], next_cell[1], matrix)

        for cell in neighbors:
            x1 = cell[0]
            y1 = cell[1]
            
            if visited_cells[x1][y1] == [False]:
                visited_cells[x1][y1] = [True]
                queue.append([x1, y1])
    
    for row in visited_cells:
        for cell in row:
            if cell == [False]:
                return False

    # If not found any unvisited cells, return True
    return True


def find_available_neighbour(x, y, matrix):
    '''Helper method for breadth_first_search(). Returns a list
    of available neighbor cells where can be move from the current
    cell.'''

    neighbors = []
    size = len(matrix)    

    if y != 0:
        # Left neighbor
        if matrix[x][y][0] == 0:
            neighbors.append([x, y-1])

    if x != 0:
        # Top neighbor
        if matrix[x][y][1] == 0:
            neighbors.append([x-1, y])

    if y != (size - 1):
        # Right neighbor
        if matrix[x][y][2] == 0:
            neighbors.append([x, y+1])

    if x != size - 1:
        # Below neighbor
        if matrix[x][y][3] == 0:
            neighbors.append([x+1, y])
    
    return neighbors


''' 
# Testikoodia

print("testi alkaa")
sokkelo = backtracker.create_bactracker_maze(4)
print("sokkelo luotu")

print("sokkelon tulostus alkaa")
for rivi in sokkelo:
    print(rivi)
print()
print("sokkelon tulostus loppu")

tulos = are_all_cells_reachable(sokkelo)
print("Tulos on luotu")
print(tulos)
'''