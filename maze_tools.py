'''Module for analyzing maze generation details'''


def count_maze_impasses(maze):
    '''Returns the amount of maze impasses e.g. how many cells include
    only one "1". Helps to analyze maze complexity.
    Can be used for recursive backtracker and aldous-broder algorithms.'''

    impasses = 0

    for row in maze:
        for cell in row:
            text = str(cell)
            if text.count("1") == 3:
                impasses += 1

    return impasses


def kruskal_maze_impasse_amount(maze):
    '''Returns the amount of maze impasses e.g. how many cells include only one "1".
    Helps to analyze maze complexity.'''

    impasses = 0

    for row in maze:
        for cell in row:
            if len(cell.open_edges) == 2:
                impasses += 1

    return impasses


def fastest_maze_generation_algorithm(backtracker_time, kruskal_time, aldous_broder_execution_time):
    '''Returns the name of the fastest algorithm and the generation time'''

    if backtracker_time < kruskal_time and backtracker_time < aldous_broder_execution_time:
        algorithm ="Recursive backtracker algorithm" 
        time = backtracker_time

    elif kruskal_time < backtracker_time and kruskal_time < aldous_broder_execution_time:
        algorithm = "Kruskal's algorithm"
        time = kruskal_time

    else: 
        algorithm = "Aldous-Broder algorithm"
        time = aldous_broder_execution_time

    result = algorithm + " in " + str(time) + " ms"

    return result


def least_impasses(backtracker_impasses, kruskal_impasses, aldous_broder_impasses):
    '''Returns the description of the algorithm that generated a maze with most impasses'''

    if backtracker_impasses <= kruskal_impasses and backtracker_impasses <= aldous_broder_impasses:

        if backtracker_impasses == kruskal_impasses and backtracker_impasses == aldous_broder_impasses:
            return "All algorithms has the same amount of impasses: " + str(kruskal_impasses) + " pcs"
        
        elif backtracker_impasses == kruskal_impasses:
            return "Recursive backtracker algorithm and Kruskal's algorithm had the same amount of impasses: " + str(kruskal_impasses) + " pcs"
        
        elif backtracker_impasses == aldous_broder_impasses:
            return "Recursive backtracker algorithm and Aldous-Broder algorithm had the same amount of impasses: " + str(backtracker_impasses) + " pcs"

        else:
            return "Recursive backtracker algorithm with " + str(backtracker_impasses) + " impasses"

    elif kruskal_impasses <= backtracker_impasses and kruskal_impasses <= aldous_broder_impasses:

        if kruskal_impasses == aldous_broder_impasses:
            return "Kruskal's algorithm and Aldous-Broder algorithm had the same amount of impasses: " + str(kruskal_impasses) + " pcs"
        
        else:
            return "Kruskal's algorithm with " + str(kruskal_impasses) + " impasses"

    else:
        return "Aldous-Broder algorithm with " + str(aldous_broder_impasses) + " impasses"
