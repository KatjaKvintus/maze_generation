'''Module app'''
from flask import Flask
from flask import render_template, request
from . import backtracker
from . import kruskal
from . import recursive_division
import time


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
    backtracker_impasses = backtracker.bactracker_maze_impasse_amount(backtracker_maze)

    # Kruskal's algorithm
    start_time = time.time()
    kruskal_maze = kruskal.create_kruskal_maze(size)
    end_time = time.time()
    kruskal_execution_time = round((end_time - start_time) * 1000, 4)
    kruskal_image = kruskal.print_kruskal_maze(size, kruskal_maze)
    kruskal_impasses = kruskal.kruskal_maze_impasse_amount(kruskal_maze)
    print("Kohta 0")

    # Recursive division algorithm
    print("Kohta 1")
    start_time = time.time()
    print("Kohta 2")
    rec_division_maze = recursive_division.create_recursive_division_maze(size)
    print("Kohta 3")
    end_time = time.time()
    print("Kohta 4")
    rec_division_execution_time = round((end_time - start_time) * 1000, 4)
    print("Kohta 5")
    #rec_division_image = recursive_division.draw_recursive_division_maze(size, rec_division_maze)
    print("Kohta 6")
    rec_division_impasses = recursive_division.rec_division_maze_impasse_amount(rec_division_maze)
    print("Kohta 7")

    return render_template("/results.html",
                           backtracker_maze=backtracker_maze,
                           backtracker_image=backtracker_image,
                           backtracker_execution_time=backtracker_execution_time,
                           backtracker_impasses=backtracker_impasses,
                           kruskal_maze=kruskal_maze,
                           kruskal_image=kruskal_image,
                           kruskal_execution_time = kruskal_execution_time,
                           kruskal_impasses=kruskal_impasses,
                           rec_division_maze=rec_division_maze,
                           rec_division_execution_time=rec_division_execution_time,
                           #rec_division_image=rec_division_image,
                           rec_division_impasses=rec_division_impasses)
