import random
import turtle
from PIL import Image


def create_recursive_division_maze(size):
    '''Create a maze of required size. In the beginning there is no walls. The list
    of 4 characters in each cell tells its wall situation.  A wall is marked by '1',
    an opening is marked by '0'. At the beginning all the cells are empty and this 
    is marked in teh list as [8, 8, 8, 8]. The cell keeps track of its walls in
    this order: left, top, right, bottom. After handling 1 is for wall and 0 is 
    for opening.'''

    # A 2D list to keep track of matrix walls
    matrix = [[[8, 8, 8, 8] for i in range(size)] for j in range(size)]

    # Add outer edges
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
    
    # Call for recursive function that keeps dividing the matrix
    divide_area(matrix, 0, 0, size - 1, size - 1, size)
    
    return matrix


def divide_area(matrix, start_x, start_y, end_x, end_y, size):
    '''Helper function for the create_recursive_division_maze.
    for dividing areas.'''
    
    # Check if the area to divide is too small
    if (end_x - start_x) < 2 or (end_y - start_y) < 2:
        return

    # Chooses a random horizontal or vertical line to divide the area
    options = ["horizontal", "vertical"]
    random_direction = random.randint(0,1)
    chosen_direction = options[random_direction]

    # Creating avertical wall
    if chosen_direction == "vertical":

        y = random.randint(start_y + 1, end_y - 1)

        for x in range(start_x, end_x + 1):
            # Seinä paikalleen
            matrix[x][y][0] = 1         # vasen seinä   
            matrix[x][y - 1][2] = 1     # oikea seinä
        
        # Lisää aukko
        matrix[x][y][0] = 0  
        matrix[x][y-1][2] = 0  

        divide_area(matrix, start_x, start_y, x - 1, end_y, size)
        divide_area(matrix, x + 1, start_y, end_x, end_y, size)

    else:
        # Pick horizontal line > create vertical opening
        x = random.randint(start_x + 1, end_x - 1)

        for y in range(start_x, end_x + 1):
            matrix[x][y][3] = 1
            matrix[x + 1][y][1] = 1
        
        # Lisää aukko
        matrix[x][y][3] = 0  
        matrix[x +1][y][1] = 0  

        divide_area(matrix, start_x, start_y, end_x, y - 1, size)
        divide_area(matrix, start_x, y + 1, end_x, end_y, size)


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
    print("Kohta 1.1.0")
    canvas = turtle.Screen()
    print("Kohta 1.1.1")
    canvas.setup(width=900, height=900)
    print("Kohta 1.1.2")
    drawer = turtle.Turtle()
    print("Kohta 1.1.3") 

    start_x = -380
    start_y = -start_x
    maze_size = (2 * (-start_x))/size
    drawer.clear()
    drawer.speed(0)
    drawer.penup()

    print("Kohta 1.2")

    # Draw part of the frame: top and right
    drawer.goto(start_x, start_y)
    drawer.pendown()
    drawer.goto(-start_x, start_y)
    drawer.goto(-start_x, -start_y)
    drawer.setheading(0)

    print("Kohta 1.3")

    # Drawing horizontal lines
    for y in range(size):
        print("Kohta 4")

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
    print("Kohta 1.5")
    #Drawing vertical lines
    drawer.left(90)

    for x in range(size):
        print("Kohta 1.6")
        drawer.penup()
        drawer.goto(start_x + maze_size * (x), -start_y)

        for y in range(size):
            if matrix[size - y - 1][x][0] == 1:
                drawer.pendown()
            else:
                drawer.penup()

            drawer.forward(maze_size)
    print("Kohta 1.7")
    image = drawer.getscreen()
    image.getcanvas().postscript(file="static/rec_division_maze.eps")
    maze_image = Image.open("static/rec_division_maze.eps")
    maze_image.save("static/rec_division_maze_image.jpg", "jpeg")
    drawer.clear()
    print("Kohta 1.8")
    return maze_image
