'''Module for analyzing maze generation details'''


def count_maze_impasses(maze):
    '''Returns the amount of maze impasses e.g. how many cells include
    only one "1". Helps to analyze maze complexity.
    Can be used for Iterative DFS and aldous-broder algorithms.'''

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


def fastest_maze_generation_algorithm(dfs_time, kruskal_time, a_b_execution_time):
    '''Returns the name of the fastest algorithm and the generation time'''

    if dfs_time < kruskal_time and dfs_time < a_b_execution_time:
        algorithm ="Iterative DFS algorithm"
        time = dfs_time

    elif kruskal_time < dfs_time and kruskal_time < a_b_execution_time:
        algorithm = "Kruskal's algorithm"
        time = kruskal_time

    else:
        algorithm = "Aldous-Broder algorithm"
        time = a_b_execution_time

    result = algorithm + " in " + str(time) + " ms"

    return result


def least_impasses(bt_impasses, kruskal_impasses, a_b_impasses):
    '''Returns the description of the algorithm that generated a maze with most impasses'''

    if bt_impasses <= kruskal_impasses and bt_impasses <= a_b_impasses:

        if bt_impasses == kruskal_impasses and bt_impasses == a_b_impasses:
            result = "All algorithms has the same amount of impasses: "
            return result + str(kruskal_impasses) + " pcs"

        if bt_impasses == kruskal_impasses:
            phrase_1 = "Iterative DFS algorithm and Kruskal's algorithm"
            phrase_2 = " had the same amount of impasses: "
            result = phrase_1 + phrase_2
            return result + str(kruskal_impasses) + " pcs"

        if bt_impasses == a_b_impasses:
            phrase_1 = "Iterative DFS algorithm and Aldous-Broder algorithm"
            phrase_2 = " had the same amount of impasses: "
            result = phrase_1 + phrase_2
            return result + str(bt_impasses) + " pcs"

        else:
            return "Iterative DFS algorithm with " + str(bt_impasses) + " impasses"

    if kruskal_impasses <= bt_impasses and kruskal_impasses <= a_b_impasses:

        if kruskal_impasses == a_b_impasses:
            phrase_1 = "Kruskal's algorithm and Aldous-Broder algorithm "
            phrase_2 = "had the same amount of impasses: "
            result = phrase_1 + phrase_2
            return result + str(kruskal_impasses) + " pcs"

        else:
            return "Kruskal's algorithm with " + str(kruskal_impasses) + " impasses"

    else:
        return "Aldous-Broder algorithm with " + str(a_b_impasses) + " impasses"
