'''Module for handling maze related functions'''



def __init__(self, size : int, type: str):
    '''Constructor for maze objects. Maze has a size (matrix side lenght)
    and type (prim, recursive backtracker, kruskal or binary tree)'''
    self.size = size
    self.type = type


def check_maze_validity(maze):
    '''This function checks if maze meets acceptance criteria
    (has at least one solution?) and returns True if the maze is adequate'''

    # Koodia tänne


