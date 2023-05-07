'''Module for generating mazes '''
import random
import turtle
from PIL import Image


def create_aldous_broder_maze(size):
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
    # False = not visited, True = has been visited. All cells are False at the beginning.
    visit_status = [[False for i in range(size)] for j in range(size)]

    # Start cell (random)
    current_x = random.randint(0, size-1)
    current_y = random.randint(0, size-1)
    current_cell = [current_x, current_y]
    visit_status[current_x][current_y] = True

    visited_cells_sum = 1
    max_visited_cells_sum = size * size


    while visited_cells_sum != max_visited_cells_sum:

        # 0 = not possible move, 1 = possible move
        move_availability = [0, 0, 0, 0]         # in oder = left, up, right, below

        if current_y != 0:
            # If there is a left neighbour
            move_availability[0] = 1

        if current_x != 0:
            # If there is a top neighbour
            move_availability[1] = 1

        if current_y != (size - 1):
            # If there is a right neighbour
            move_availability[2] = 1

        if current_x != size - 1:
            # If there is a bottom neighbour
            move_availability[3] = 1

        move_handled = False

        while move_handled is False:

            drawn_direction = random.randint(0, 3)

            if move_availability[drawn_direction] == 1:

                # If you go to the cell in your left
                if drawn_direction == 0:

                    if visit_status[current_x][current_y-1] is False:
                        # If this cell has not been visited yet, remove the
                        # left wall from current cell and the right wall
                        # from the cell on your left
                        matrix[current_cell[0]][current_cell[1]][0] = 0
                        matrix[current_cell[0]][current_cell[1] - 1][2] = 0

                    next_cell = [current_cell[0], current_cell[1] - 1]


                # If you go to the cell above you
                elif drawn_direction == 1:

                    # If this cell has not been visited yet, remove the wall
                    # above from the current cell the wall below from the cell
                    # above you
                    if visit_status[current_x-1][current_y] is False:
                        matrix[current_cell[0]][current_cell[1]][1] = 0
                        matrix[current_cell[0] - 1][current_cell[1]][3] = 0

                    next_cell = [current_cell[0] - 1, current_cell[1]]

                # If you go to the cell in your right
                elif drawn_direction == 2:

                    # If this cell has not been visited yet, remove right wall
                    # from current cell and left wall from the next cell
                    if visit_status[current_x][current_y+1] is False:
                        matrix[current_cell[0]][current_cell[1]][2] = 0
                        matrix[current_cell[0]][current_cell[1] + 1][0] = 0

                    next_cell = [current_cell[0], current_cell[1] + 1]

                # If you go to the cell below you
                else:
                    # If this cell has not been visited yet, remove the wall below
                    # from current cell and remove the wall top from the next cell
                    if visit_status[current_x+1][current_y] is False:
                        matrix[current_cell[0]][current_cell[1]][3] = 0
                        matrix[current_cell[0] + 1][current_cell[1]][1] = 0

                    next_cell = [current_cell[0] + 1, current_cell[1]]

                if visit_status[current_cell[0]][current_cell[1]] is False:

                    # If this was 1st time in this cell, mark it as visited
                    visit_status[current_cell[0]][current_cell[1]] = True
                    visited_cells_sum += 1

                current_cell = next_cell

                current_x = current_cell[0]
                current_y = current_cell[1]

                move_handled = True

    return matrix



def draw_aldous_broder_maze_image(size, matrix):
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
    image.getcanvas().postscript(file="static/aldous_broder__maze.eps")
    maze_image = Image.open("static/aldous_broder__maze.eps")
    maze_image.save("static/aldous_broder_maze_image.jpg", "jpeg")
    drawer.clear()
    #canvas.bye()

    return maze_image
