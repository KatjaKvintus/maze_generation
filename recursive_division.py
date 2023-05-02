import random
import turtle
#from PIL import Image


def create_recursive_division_maze(size):
    '''Creates a maze of required size. In the beginning there is no walls. The list
    of 4 characters in each cell tells its wall situation.  A wall is marked by '1',
    an opening is marked by '0'. At the beginning all the cells are empty and this 
    is marked in the list as [0, 0, 0, 0]. The cell keeps track of its walls in
    this order: left, top, right, bottom. After handling 1 is for wall and 0 is 
    for opening.'''

    # A 2D list to keep track of matrix walls. x for rows, y for columns.
    matrix = [[[0, 0, 0, 0] for i in range(size)] for j in range(size)]

    # Add frame (outer edges)
    row = 0
    column = 0

    while row < size:
        column = 0

        while column < size:

            if row == 0:
                matrix[row][column][1] = 1      # top
            if row == size - 1:
                matrix[row][column][3] = 1      #bottom
            if column == 0:
                matrix[row][column][0] = 1      # left
            if column == size - 1:
                matrix[row][column][2] = 1      # right

            column += 1
        row += 1
    
    # Call for thr recursive function that keeps dividing the matrix
    divide_area(matrix, 0, 0, size -2, size - 2, choose_orientation(size - 1, size - 1))
    
    return matrix


#####################################################################

def divide_area(matrix, start_x, start_y, end_x, end_y, orientation):
    '''Helper function for the create_recursive_division_maze.
    for dividing areas.'''
    
    print(f"start: ({start_x},{start_y}), end: ({end_x},{end_y})")
    print(f"end_x - start_x = {end_x} - {start_x} = {end_x - start_x}") ################
    print(f"end_y - start_y = {end_y} - {start_y} = {end_y - start_y}") ################

    # Check if the area to divide is too small (< 2)
    if (end_x - start_x) < 2 or (end_y - start_y) < 2:
        print("Katkaisuehto täyttyi") ###############################
        print() ###############################
        return

    print("Suunta: ", orientation) ##############

    if orientation == "horizontal":             # VAAKASUORA VIIVA, eli x pysyy samana 

        # Choose random x for inserting a horizontal wall
        wall_x = random.randint(start_x, end_x - 1)

        # Add a wall 
        for y in range(start_y, end_y + 1):
            matrix[wall_x][y][3] = 1
            matrix[wall_x + 1][y][1] = 1

        # Add an opening into that wall i.e. "the sledgehammer"
        random_y = random.randint(start_y, end_y)
        matrix[wall_x][random_y][3] = 0
        matrix[wall_x + 1][random_y][1] = 0
        print("Vaakasuora viiva lisätty rivin ", wall_x, "alle") ############
        print() ###############################

        # Divide the maze above and below the wall
        print(f"Rekursiivinen kutsu 1: ({start_x},{start_y}) - ({wall_x - 1},{end_y})") ###############
        divide_area(matrix, start_x, start_y, wall_x - 1, end_y, 
                    choose_orientation(wall_x - start_x, end_y - start_y + 1))
        
        print(f"Rekursiivinen kutsu 2: ({wall_x + 1},{start_y}) - ({end_x},{end_y})") ###############
        divide_area(matrix, wall_x + 1, start_y, end_x, end_y, 
                    choose_orientation(end_x - wall_x + 1, end_y - start_y + 1))


    # Creating a vertical wall (left side of the cell)
    else:                 # PYSTYSUORA VIIVA, eli y pysyy samana 

        # Choose a random point to place a vertical wall
        wall_y = random.randint(start_y, end_y - 1)

        # Add a wall 
        for x in range(start_x, end_x + 1):
            matrix[x][wall_y][0] = 1
            matrix[x][wall_y - 1][2] = 1

        # Add opening to the just built wall
        random_x = random.randint(start_x, end_x)
        matrix[random_x][wall_y][0] = 0
        matrix[random_x][wall_y - 1][2] = 0
        print("Pystyviiva lisätty sarakkeen ", wall_y, " vasemmalle puolelle") ############
        print() ###############################

        # Divide the maze left and right of the wall
        divide_area(matrix, start_x, start_y, end_x, wall_y - 1, 
                    choose_orientation(end_x - start_x + 1, wall_y- start_y))
        
        divide_area(matrix, start_x, wall_y + 1, end_x, end_y, 
                    choose_orientation(end_x - start_x + 1, end_y - wall_y))

#####################################################################


def choose_orientation(width, height):
    '''For drawing a direction for the next round of building walls'''

    if width < height:
        return "horizontal"
    elif height < width:
        return "vertical"
    else:
        return random.choice(["horizontal", "vertical"])


def rec_division_maze_impasse_amount(maze):
    '''Returns the amount of maze impasses e.g. how many cells include only one "1".
    Helps to analyze maze complexity.'''

    impasses = 0

    for row in maze:
        for cell in row:
            text = str(cell)
            if text.count("1") == 1:
                impasses += 1

    return impasses


def draw_recursive_division_maze(size, matrix):
    '''Draws maze image'''
    canvas = turtle.Screen()
    canvas.setup(width=900, height=900)
    drawer = turtle.Turtle()

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
            else:
                print("error")

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
    image.getcanvas().postscript(file="static/rec_division_maze.eps")
    maze_image = Image.open("static/rec_division_maze.eps")
    maze_image.save("static/rec_division_maze_image.jpg", "jpeg")
    drawer.clear()

    return maze_image


''' 
# TESTIKOODIA
print()
sokkelo = create_recursive_division_maze(8)
print()
for rivi in sokkelo:
    print(rivi)
'''

