'''Module fo bactracking algorithm maze generation and visualization'''
import random
import turtle
from PIL import Image


def create_dfs_maze(size: int):
    '''Create a maze of required size. In the beginning every cell has walls around it.
    The list of 4 characters in each cell tells its wall situation.  A wall is marked
    by '1', a lack of wall is marked by '0'. At the beginning all walls are up so every
    cell contains a list of [1, 1, 1, 1]. The cell keeps track of its walls in this order:
    left, top, right, bottom. '''

    # Check that parameter is the rght type (integer) and right
    # size: 4 <= n <= 200
    if not isinstance(size, int):
        return "Incorrect parameter type"
    if int(size) < 4:
        return "Too small parameter"
    if size > 200:
        return "Too big parameter"


    # A 2D list to keep track of matrix walls
    matrix = [[[1, 1, 1, 1] for i in range(size)] for j in range(size)]

    # Another 2D list that keeps track of which cells has been visited. Same size as the matrix.
    # 0 = not visited, 1 = has been visited. All cells are 0 at the beginning.
    visit_status = [[0 for i in range(size)] for j in range(size)]

    pos_x = 0
    pos_y = 0

    # Starting point is (0, 0): top left corner
    current_cell = [pos_x, pos_y]

    visited_cells_sum = 1
    max_visited_cells_sum = size * size

    #Cells in visit order. Needed for backing up from an impasse.
    cell_stack = []

    cell_stack.append([pos_x, pos_y])     # adding the starting point

    visit_status[pos_x][pos_y] = 1      # marking the starting point as a visited one

    while visited_cells_sum != max_visited_cells_sum:

        # 0 = not possible move, 1 = possible move
        move_availability = [0, 0, 0, 0]         # in oder = left, up, right, below

        if pos_y != 0:
            # If it is possible to move left
            if visit_status[pos_x][pos_y-1] == 0:
                move_availability[0] = 1

        if pos_x != 0:
            # If it is possible to  move up
            if visit_status[pos_x-1][pos_y] == 0:
                move_availability[1] = 1

        if pos_y != (size - 1):
            # If it is possible to  move right
            if visit_status[pos_x][pos_y+1] == 0:
                move_availability[2] = 1

        if pos_x != size - 1:
            # If it is possible to move below
            if visit_status[pos_x+1][pos_y] == 0:
                move_availability[3] = 1

        if move_availability == [0, 0, 0, 0]:
            # If no moves available', return to the latest cell in the stack

            if visit_status[current_cell[0]][current_cell[1]] == 0:
                visited_cells_sum += 1

            visit_status[current_cell[0]][current_cell[1]] = 1

            if current_cell == cell_stack[len(cell_stack) - 1]:
                cell_stack.pop()    # Remove current cell from the stack

            top_of_cell_stack = cell_stack.pop()
            pos_x = top_of_cell_stack[0]
            pos_y = top_of_cell_stack[1]
            current_cell = [pos_x, pos_y]

        else:
            move_handled = False

            while move_handled is False:

                drawn_direction = random.randint(0, 3)

                if move_availability[drawn_direction] == 1:

                    if drawn_direction == 0:
                        # moves into cell on the left, removes left wall from current cell,
                        # removes right wall from the next cell
                        next_cell = [current_cell[0], current_cell[1] - 1]
                        matrix[current_cell[0]][current_cell[1]][0] = 0
                        matrix[next_cell[0]][next_cell[1]][2] = 0

                    elif drawn_direction == 1:
                        # moves into cell above, removes wall above from current cell,
                        # removes wall below from the next cell
                        next_cell = [current_cell[0] - 1, current_cell[1]]
                        matrix[current_cell[0]][current_cell[1]][1] = 0
                        matrix[next_cell[0]][next_cell[1]][3] = 0

                    elif drawn_direction == 2:
                        # moves into cell on the right, removes right wall from current cell,
                        # removes left wall from the next cell
                        next_cell = [current_cell[0], current_cell[1] + 1]
                        matrix[current_cell[0]][current_cell[1]][2] = 0
                        matrix[next_cell[0]][next_cell[1]][0] = 0

                    else:
                        # moves into cell below, removes wall below from current cell,
                        # removes wall top from the next cell
                        next_cell = [current_cell[0] + 1, current_cell[1]]
                        matrix[current_cell[0]][current_cell[1]][3] = 0
                        matrix[next_cell[0]][next_cell[1]][1] = 0

                    if visit_status[current_cell[0]][current_cell[1]] == 0:
                        # If this was 1st time in this cell, mark as visited
                        visited_cells_sum += 1

                    visit_status[current_cell[0]][current_cell[1]] = 1
                    cell_stack.append(next_cell)
                    current_cell = next_cell

                    pos_x = current_cell[0]
                    pos_y = current_cell[1]
                    move_handled = True

    return matrix


def draw_maze_image(size, matrix):
    '''Draws maze image'''

    drawer = turtle.Turtle()
    canvas = turtle.Screen()
    canvas.setup(width=900, height=900)

    start_x = -380
    start_y = -start_x
    maze_size = (2 * (-start_x))/size
    drawer.clear()
    drawer.speed(0)
    drawer.penup()

    # Draw part of the frame: top and right
    drawer.goto(start_x, start_y)
    drawer.pendown()
    drawer.goto(-start_x, start_y)
    drawer.goto(-start_x, -start_y)
    drawer.setheading(0)

    # Drawing horizontal lines
    for y in range(size):

        drawer.penup()
        drawer.goto(start_x, start_y + -maze_size * (y) - maze_size)

        for x in range(size):

            if matrix[y][x][3] == 1:
                drawer.pendown()
            elif matrix[y][x][3] == 0:
                drawer.penup()

            drawer.forward(maze_size)

    #Drawing vertical lines
    drawer.left(90)

    for x in range(size):

        drawer.penup()
        drawer.goto(start_x + maze_size * (x), -start_y)

        for y in range(size):
            if matrix[size - y - 1][x][0] == 1:
                drawer.pendown()
            else:
                drawer.penup()

            drawer.forward(maze_size)

    image = drawer.getscreen()
    image.getcanvas().postscript(file="static/dfs_maze.eps")
    maze_image = Image.open("static/dfs_maze.eps")
    maze_image.save("static/dfs_maze_image.jpg", "jpeg")
    drawer.clear()

    return maze_image
