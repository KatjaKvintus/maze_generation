'''A Module for analyzing maze paths'''
from collections import deque
from . import kruskal


def show_kruskal_maze_as_2_D_list(maze):
    '''A helper function to show Kruskal's maze same way as
    DFS and Aldous-Broder (a 2D list, each cell containing a 4 character
    binary list: 1 = wall, 0 = door).'''

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


def are_all_cells_reachable(matrix):
    '''Returns True if BFS can visits every cell in the maze that is modeled as
    a 2D array (like DFS and Aldous-Broder, or Kruskal after using
    show_kruskal_maze_as_2D_list() function)'''

    visited_cells = breadth_first_search(matrix)

    for row in visited_cells:

        for cell in row:

            if cell is False:
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

        # Neigbors = availeble slots right next to the current cell that
        # are available to move to.
        neighbors = find_available_neighbour(next_cell[0], next_cell[1], matrix)

        for cell in neighbors:
            x_1 = cell[0]
            y_1 = cell[1]

            if visited_cells[x_1][y_1] is False:
                visited_cells[x_1][y_1] = True
                queue.append([x_1, y_1])

    return visited_cells


def find_available_neighbour(pos_x, y, matrix):
    '''Helper method for breadth_first_search(). Returns a list of available
    neighbor cells where can be move from the current cell.'''

    neighbors = []
    size = len(matrix)

    if y != 0:
        # Left neighbor
        if matrix[pos_x][y][0] == 0:
            neighbors.append([pos_x, y-1])

    if pos_x != 0:
        # Top neighbor
        if matrix[pos_x][y][1] == 0:
            neighbors.append([pos_x-1, y])

    if y != (size - 1):
        # Right neighbor
        if matrix[pos_x][y][2] == 0:
            neighbors.append([pos_x, y+1])

    if pos_x != size - 1:
        # Below neighbor
        if matrix[pos_x][y][3] == 0:
            neighbors.append([pos_x+1, y])

    return neighbors


def maze_type(maze):
    '''Returns "perfect maze" if all maze cells are reachable, and
    "non-perfect" if not. Needed for UI.'''

    if are_all_cells_reachable(maze):
        return "perfect maze"
    return "non-perfect maze"


def shortest_path(matrix):
    '''For finding the shortest path in a 2D matrix. If path is available,
    returns path length. If not, returns -1.'''

    size = len(matrix)
    distances = [[1000 for i in range(size)] for j in range(size)]
    distances[0][0] = 0
    start = [0, 0]

    # A queue for keeping track of the cell neighbors go-through.
    queue = []
    queue = deque([start])

    # Another 2D list to keep tracke which cells have been visited.
    # False = not visited, True = visited
    visited_squares = [[False for i in range(size)] for j in range(size)]
    visited_squares[0][0] = True

    while len(queue) > 0:

        next_cell = queue.popleft()
        x = next_cell[0]
        y = next_cell[1]
        visited_squares[x][y] = True

        # Update the distances of neighbors
        neighbors = find_available_neighbour(x, y, matrix)

        for cell in neighbors:
            x_1 = cell[0]
            y_1 = cell[1]

            if visited_squares[cell[0]][cell[1]] is False:

                visited_squares[x_1][y_1] = True
                distances[x_1][y_1] = distances[x][y] + 1
                queue.append(cell)

    if distances[size-1][size-1] != 1000:
        return distances[size-1][size-1]
    return -1


def find_shortest_path_of_three(dfs, kruskal, aldous_broder):
    '''Returns the description of the algorithm that generated a maze
    with the shortest path'''

    if dfs <= kruskal and dfs <= aldous_broder:

        if dfs == kruskal and dfs == aldous_broder:
            result = "All mazes have equally short shortest path: "
            return result + str(kruskal) + " steps"

        if dfs == kruskal:
            phrase_1 = "Iterative DFS maze and Kruskal's maze"
            phrase_2 = " had equally short shortest path: "
            result = phrase_1 + phrase_2
            return result + str(kruskal) + " steps"

        if dfs == aldous_broder:
            phrase_1 = "Iterative DFS maze and Aldous-Broder maze"
            phrase_2 = " had equally short shortest path: "
            result = phrase_1 + phrase_2
            return result + str(dfs) + " steps"

        return "Iterative DFS maze with " + str(dfs) + " steps"

    if kruskal <= dfs and kruskal <= aldous_broder:

        if kruskal == aldous_broder:
            phrase_1 = "Kruskal's maze and Aldous-Broder maze had "
            phrase_2 = "equally short shortest path: "
            result = phrase_1 + phrase_2
            return result + str(kruskal) + " steps"

        return "Kruskal's maze with " + str(kruskal) + " steps"

    return "Aldous-Broder maze with " + str(aldous_broder) + " steps"
