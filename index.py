'''Module index'''

import time
from flask import Flask
from flask import render_template, request
from . import dfs, kruskal, aldous_broder, maze_tools, maze_paths

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    '''Route: index.html'''
    return render_template("index.html")


@app.route("/generate_mazes", methods=["GET", "POST"])
def generate_mazes():
    '''Handles users choices of algorithms for comparison'''

    size = request.form["maze_size"]
    size = int(size)

    # DFS algorithm
    start_time = time.time()
    dfs_maze = dfs.create_dfs_maze(size)
    end_time = time.time()
    dfs_execution_time = round((end_time - start_time) * 1000, 4)
    dfs.draw_maze_image(size, dfs_maze)
    dfs_impasses = maze_tools.count_maze_impasses(dfs_maze)
    dfs_type = maze_paths.maze_type(dfs_maze)
    dfs_shortest_path = maze_paths.shortest_path(dfs_maze)

    # Kruskal's algorithm
    start_time = time.time()
    kruskal_maze = kruskal.create_kruskal_maze(size)
    end_time = time.time()
    kruskal_execution_time = round((end_time - start_time) * 1000, 4)
    kruskal.print_kruskal_maze(size, kruskal_maze)
    kruskal_maze_as_2_D_list = maze_paths.show_kruskal_maze_as_2_D_list(kruskal_maze)
    kruskal_impasses = maze_tools.count_maze_impasses(kruskal_maze_as_2_D_list)
    kruskal_type = maze_paths.maze_type(kruskal_maze_as_2_D_list)
    kruskal_shortest_path = maze_paths.shortest_path(kruskal_maze_as_2_D_list)

    # Aldous-Broder algorithm
    start_time = time.time()
    aldous_broder_maze = aldous_broder.create_aldous_broder_maze(size)
    end_time = time.time()
    aldous_broder_execution_time = round((end_time - start_time) * 1000, 4)
    aldous_broder.draw_aldous_broder_maze_image(size, aldous_broder_maze)
    aldous_broder_impasses = maze_tools.count_maze_impasses(aldous_broder_maze)
    aldous_broder_type = maze_paths.maze_type(aldous_broder_maze)
    aldous_broder_shortest_path = maze_paths.shortest_path(aldous_broder_maze)


    # For resuls summary
    fastest = maze_tools.fastest_maze_generation_algorithm(dfs_execution_time,
                                                      kruskal_execution_time,
                                                      aldous_broder_execution_time)
    least_impasses = maze_tools.least_impasses(dfs_impasses,
                                                  kruskal_impasses, aldous_broder_impasses)
    shortest_path = maze_paths.find_shortest_path_of_three(dfs_shortest_path,
                                                           kruskal_shortest_path,
                                                           aldous_broder_shortest_path)


    return render_template("/results.html",
                           dfs_execution_time=dfs_execution_time,
                           dfs_impasses=dfs_impasses,
                           dfs_type=dfs_type,
                           dfs_shortest_path=dfs_shortest_path,
                           kruskal_execution_time = kruskal_execution_time,
                           kruskal_impasses=kruskal_impasses,
                           kruskal_type=kruskal_type,
                           kruskal_shortest_path=kruskal_shortest_path,
                           aldous_broder_execution_time=aldous_broder_execution_time,
                           aldous_broder_impasses=aldous_broder_impasses,
                           aldous_broder_type=aldous_broder_type,
                           aldous_broder_shortest_path=aldous_broder_shortest_path,
                           fastest=fastest,
                           least_impasses=least_impasses,
                           shortest_path=shortest_path)
