'''Module index'''

from flask import Flask
from flask import render_template, request
import time
from . import backtracker, kruskal, aldous_broder, maze_tools

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

    # Bactracker algorithm
    start_time = time.time()
    backtracker_maze = backtracker.create_bactracker_maze(size)
    end_time = time.time()
    backtracker_execution_time = round((end_time - start_time) * 1000, 4)
    backtracker_image = backtracker.draw_maze_image(size, backtracker_maze)
    backtracker_impasses = maze_tools.count_maze_impasses(backtracker_maze)

    # Kruskal's algorithm
    start_time = time.time()
    kruskal_maze = kruskal.create_kruskal_maze(size)
    end_time = time.time()
    kruskal_execution_time = round((end_time - start_time) * 1000, 4)
    kruskal_image = kruskal.print_kruskal_maze(size, kruskal_maze)
    kruskal_impasses = maze_tools.kruskal_maze_impasse_amount(kruskal_maze)

    # Aldous-Broder algorithm
    start_time = time.time()
    aldous_broder_maze = aldous_broder.create_aldous_broder_maze(size)
    end_time = time.time()
    aldous_broder_execution_time = round((end_time - start_time) * 1000, 4)
    aldous_broder_image = aldous_broder.draw_aldous_broder_maze_image(size, aldous_broder_maze)
    aldous_broder_impasses = maze_tools.count_maze_impasses(aldous_broder_maze)


    # For resuls summary
    fastest = maze_tools.fastest_maze_generation_algorithm(backtracker_execution_time, 
                                                      kruskal_execution_time, aldous_broder_execution_time)
    least_impasses = maze_tools.least_impasses(backtracker_impasses, 
                                                  kruskal_impasses, aldous_broder_impasses)


    return render_template("/results.html",
                           backtracker_execution_time=backtracker_execution_time,
                           backtracker_impasses=backtracker_impasses,
                           kruskal_execution_time = kruskal_execution_time,
                           kruskal_impasses=kruskal_impasses,
                           aldous_broder_execution_time=aldous_broder_execution_time,
                           aldous_broder_impasses=aldous_broder_impasses,
                           fastest=fastest,
                           least_impasses=least_impasses)

