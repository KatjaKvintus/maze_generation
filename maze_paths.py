'''A Module for analyzing maze paths'''



def are_all_cells_reachable(matrix):
    '''Returns True if BFS can visits every cell in the maze
    that is modeled as a 2D array (like DFS and Aldous-Broder)'''
    
    visited_cells = breadth_first_search(matrix)
    
    for row in visited_cells:
        
        print("Checkpoint 1")
        
        for cell in row:
            
            print(f"DEBUG: cellin arvo on ", cell)
            
            if cell == False:
                return False

    # If not found any unvisited cells, return True
    return True




def breadth_first_search(matrix):
    '''BFS algorithm, a helper method for are_all_cells_reachable().
    Returns True is all cells are visited during search.'''
    
    size = len(matrix)

    # List to keep track of visited nodes.
    visited_cells = [[False for i in range(size)] for j in range(size)]
    visited_cells[0][0] = True

    queue = []
    queue.append([0, 0])

    # Continue as long as queue has cells to visit
    while len(queue) > 0:

        next_cell = queue.pop(0)

        neighbors = find_available_neighbour(next_cell[0], next_cell[1], matrix)

        for cell in neighbors:
            x1 = cell[0]
            y1 = cell[1]

            if visited_cells[x1][y1] == False:
                visited_cells[x1][y1] = True
                queue.append([x1, y1])

    return visited_cells


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



#def find_shortest_route_in_2d_array(matrix):
    '''An algorithm for finding the shortest route in a maze that is modeled as
    a 2D array, such as iterative DFS and Aldous-Broder algorithm in this app).
    We assume that the start point is top left corner and end point is
    bottom right corner.'''

 #   cell_queue = 


