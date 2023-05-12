'''A Module for analyzing maze paths'''
import kruskal



def are_all_cells_reachable(matrix):
    '''Returns True if BFS can visits every cell in the maze
    that is modeled as a 2D array (like DFS and Aldous-Broder)'''

    visited_cells = breadth_first_search(matrix)

    for row in visited_cells:

        for cell in row:

            if cell == False:
                return False

    # If not found any unvisited cells, return True
    return True



def breadth_first_search(matrix):
    '''BFS algorithm, a helper method for are_all_cells_reachable().
    Returns a list of visited cells (True = visited, False = not visited).'''

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



def are_all_cells_reachable_in_kruskal_maze(matrix):
    '''Check that all kruskal matrix cells are reachable. Returns
    True if it is.'''

    visited_cells = set()
    
    # Starting point
    position = (0, 0)

    dfs(matrix, visited_cells, position)

    if len(visited_cells) == len(matrix * matrix):
        return True
    else:
        return False


def dfs(matrix, visited_cells, position):
    '''Depth-first search - helper function for are_all_cells_reachable_in_kruskal_maze'''

    visited_cells.add(position)

    for neighbor in matrix[position[0]][position[1]]:
        if neighbor not in visited_cells:
            dfs(matrix, visited_cells, neighbor)



def show_kruskal_maze_as_2D_list(maze):
    '''A helper function to show Kruskal's maze same way as
    DFS and Aldous-Broder'''

    size = len(maze)
    matrix = [[[1, 1, 1, 1] for i in range(size)] for j in range(size)]

    edges = kruskal.edges

    for edge in edges:
        if edge.is_open:
            start_x = edge.start_cell.pos_x
            start_y = edge.start_cell.pos_y
            end_x = edge.end_cell.pos_x
            end_y = edge.end_cell.pos_y

        if start_x == end_x - 1:
            matrix[start_x][start_y][3] = 0
            matrix[end_x][end_y][1] = 0

        elif start_y == end_y - 1:
            matrix[start_x][start_y][2] = 0
            matrix[end_x][end_y][0] = 0
        
        elif start_y == end_y + 1:
            matrix[start_x][start_y][0] = 0
            matrix[end_x][end_y][2] = 0
        
        elif start_x == end_x + 1:
            matrix[start_x][start_y][1] = 0
            matrix[end_x][end_y][3] = 0
    
    return matrix



# TESTIKOODIA

maze = kruskal.create_kruskal_maze(4)

for rivi in maze:
    for cell in rivi:
        for edge in cell.open_edges:
            print(f"Kaari ({edge.start_cell.pos_x},{edge.start_cell.pos_y}) - ({edge.end_cell.pos_x},{edge.end_cell.pos_y})")

maze_2d = show_kruskal_maze_as_2D_list(maze)

for rivi in maze_2d:
    print(rivi)





