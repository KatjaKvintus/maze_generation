'''Module for analyzing maze generation details'''


def count_maze_impasses(maze):
    '''Returns the amount of maze impasses e.g. how many cells includes
    exactly 3 1's (=walls). Helps to analyze the maze complexity.'''

    impasses = 0

    for row in maze:
        for cell in row:
            text = str(cell)
            if text.count("1") == 3:
                impasses += 1

    return impasses


def fastest_maze_generation_algorithm(dfs_time, kruskal_time, a_b_execution_time):
    '''Returns the name of the fastest algorithm and the generation time
    of the algorithm.'''

    if dfs_time < kruskal_time and dfs_time < a_b_execution_time:
        algorithm = "Iterative DFS algorithm"
        time = dfs_time

    elif kruskal_time < dfs_time and kruskal_time < a_b_execution_time:
        algorithm = "Kruskal's algorithm"
        time = kruskal_time

    else:
        algorithm = "Aldous-Broder algorithm"
        time = a_b_execution_time

    result = algorithm + " in " + str(time) + " ms"

    return result


def least_impasses(dfs_impasses, kruskal_impasses, a_b_impasses):
    '''Returns the description of the algorithm that generated a maze
    with most impasses. Nede for UI.'''

    if dfs_impasses <= kruskal_impasses and dfs_impasses <= a_b_impasses:

        if dfs_impasses == kruskal_impasses and dfs_impasses == a_b_impasses:
            result = "All algorithms has the same amount of impasses: "
            return result + str(kruskal_impasses) + " pcs"

        if dfs_impasses == kruskal_impasses:
            phrase_1 = "Iterative DFS algorithm and Kruskal's algorithm"
            phrase_2 = " had the same amount of impasses: "
            result = phrase_1 + phrase_2
            return result + str(kruskal_impasses) + " pcs"

        if dfs_impasses == a_b_impasses:
            phrase_1 = "Iterative DFS algorithm and Aldous-Broder algorithm"
            phrase_2 = " had the same amount of impasses: "
            result = phrase_1 + phrase_2
            return result + str(dfs_impasses) + " pcs"

        return "Iterative DFS algorithm with " + str(dfs_impasses) + " impasses"

    if kruskal_impasses <= dfs_impasses and kruskal_impasses <= a_b_impasses:

        if kruskal_impasses == a_b_impasses:
            phrase_1 = "Kruskal's algorithm and Aldous-Broder algorithm "
            phrase_2 = "had the same amount of impasses: "
            result = phrase_1 + phrase_2
            return result + str(kruskal_impasses) + " pcs"

        return "Kruskal's algorithm with " + str(kruskal_impasses) + " impasses"

    else:
        return "Aldous-Broder algorithm with " + str(a_b_impasses) + " impasses"
