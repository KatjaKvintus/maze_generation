'''Module for randomized Kruskal's algorithm maze generation'''
import random
import turtle
from PIL import Image


# A global list of all edges in Kruskal maze
edges = []


class Cell:
    '''Module for handling cell related functions'''

    def __init__(self, pos_x, pos_y):
        # x and y = coordinates in matrix
        # open_edges = list of open edges to and from the cell
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.open_edges = []
        self.set = set((pos_y, pos_y))

    def get_open_edges(self):
        '''Returns a list of all open edges from this cell'''
        return self.open_edges


class Edge:
    '''Module for handling edge related functions'''

    def __init__(self, start_cell, end_cell):
        # start_cell and end_cell define edge start and ending point
        # is_open is True, if edge is open, and False, if not. At start
        # every edge is closed.
        self.start_cell = start_cell
        self.end_cell = end_cell
        self.is_open = False


def open_edge(edge):
    '''Marks and edge open and adds it to both start and end cells
    open edges list'''

    reversed_edge = Edge(edge.end_cell, edge.start_cell)

    (edge.start_cell).open_edges.append(edge)
    (edge.start_cell).open_edges.append(reversed_edge)
    (edge.end_cell).open_edges.append(edge)
    (edge.end_cell).open_edges.append(reversed_edge)


def add_edge(start, end):
    '''For adding available edges to the maze'''
    if start != end:
        edges.append(Edge(start, end))
        edges.append(Edge(end, start))


def create_kruskal_maze(size):
    '''Create a maze of required size. In the beginning every cell has walls around it.
    The list of 4 characters in each cell tells its wall situation.  A wall is marked
    by '1', a lack of wall is marked by '0'. At the beginning all walls are up so every
    cell contains a list [1, 1, 1, 1]. The cell keeps track of its walls in this order:
    left, top, right, bottom. '''

    # Check that parameter is the rght type (integer) and right
    # size: 4 <= n <= 200
    if not isinstance(size, int):
        return "Incorrect parameter type"
    if int(size) < 4:
        return "Too small parameter"
    if size > 200:
        return "Too big parameter"

    # Clear egdes list (issue only when creating several mazes in a row)
    edges.clear()

    # A 2D list to keep track of matrix cells and walls.
    matrix = []

    for pos_x in range(size):
        row = []
        for pos_y in range(size):
            row.append(Cell(pos_x, pos_y))
        matrix.append(row)


    #Adding edges to list
    for pos_x in range(size):
        for pos_y in range (size):

            start_cell = matrix[pos_x][pos_y]

            if pos_x != 0:
                end_cell = matrix[pos_x - 1][pos_y]
                add_edge(start_cell, end_cell)

            if pos_x != size -1:
                end_cell = matrix[pos_x + 1][pos_y]
                add_edge(start_cell, end_cell)

            if pos_y != 0:
                end_cell = matrix[pos_x][pos_y - 1]
                add_edge(start_cell, end_cell)

            if pos_y != size - 1:
                end_cell = matrix[pos_x][pos_y + 1]
                add_edge(start_cell, end_cell)

    # Shuffle edges in random order (because that's whats Kruskal's algorithm requires)
    random.shuffle(edges)

    # Creating sets - at the begingnning every cell is in their own set.
    # So there is size^2 sets.
    for pos_x in range(size):
        for pos_y in range(size):
            matrix[pos_x][pos_y].set = set([(pos_x, pos_y)])

    # Merging sets by removing walls one by one until there is only one set
    # containing all cells = labyrinth
    i = 0

    while i < len(edges):

        # Check if a cell set size is size^2, all cells are in the same set
        # and this loop can be stopped
        if len(edges[i].start_cell.set) == size * size:
            break

        cell_1 = edges[i].start_cell
        cell_2 = edges[i].end_cell

        if cell_1.set != cell_2.set:

            # Open the edge both ways
            open_edge(edges[i])
            edges[i].is_open = True

            # Transfer smaller set to the bigger set
            if len(cell_1.set) < len(cell_2.set):
                cell_2.set |= cell_1.set

                for item in cell_1.set:
                    matrix[item[0]][item[1]].set = cell_2.set

            else:
                cell_1.set |= cell_2.set

                for item in cell_2.set:
                    matrix[item[0]][item[1]].set = cell_1.set
        i += 1

    return matrix


def print_kruskal_maze(side_lenght, maze):
    '''Provides an image of the maze generated in Kruskal's algorithm.'''

    canvas = turtle.Screen()
    canvas.setup(width=900, height=900)

    drawer = turtle.Turtle()

    start_x = -380
    start_y = -start_x
    maze_size = int(2 * (-start_x)/side_lenght)
    drawer.clear()
    drawer.speed(0)
    drawer.penup()

    # Draw part of the frame: top and right
    drawer.goto(start_x, start_y)
    drawer.pendown()
    drawer.goto(-start_x, start_y)
    drawer.goto(-start_x, -start_y)
    drawer.goto(start_x, -start_y)
    drawer.goto(start_x, start_y)
    drawer.setheading(0)

    # Drawing horizontal lines
    for x in range(side_lenght - 1):

        drawer.penup()
        drawer.goto(start_x, start_y - maze_size * x - maze_size)

        for y in range(side_lenght):

            list_of_open_edges = maze[x][y].get_open_edges()

            for edge in list_of_open_edges:

                opening_found = False

                if edge.start_cell.pos_x == x:
                    if edge.start_cell.pos_y == y:
                        if edge.end_cell.pos_x == (x+1):
                            if edge.end_cell.pos_y == y:
                                opening_found = True
                                break

            if opening_found:
                drawer.penup()
            else:
                drawer.pendown()

            drawer.forward(maze_size)


    #Drawing vertical lines
    drawer.right(90)

    for y in range(side_lenght - 1):

        drawer.penup()
        #drawer.goto(start_x + (maze_size * -y) - maze_size, start_y)
        drawer.goto(start_x + (maze_size * y) + maze_size, start_y)


        for x in range(side_lenght):

            list_of_open_edges = maze[x][y].get_open_edges()

            for edge in list_of_open_edges:

                opening_found = False

                if edge.start_cell.pos_x == x:
                    if edge.start_cell.pos_y == y:
                        if edge.end_cell.pos_x == x:
                            if edge.end_cell.pos_y == (y + 1):
                                opening_found = True
                                break

            if opening_found:
                drawer.penup()
            else:
                drawer.pendown()

            drawer.forward(maze_size)

    maze_image = drawer.getscreen()
    maze_image.getcanvas().postscript(file="static/kruskal_maze.eps")
    maze_image = Image.open("static/kruskal_maze.eps")
    maze_image.save("static/kruskal_maze_image.jpg", "jpeg")

    drawer.clear()

    return maze_image
