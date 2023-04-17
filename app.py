'''Module app'''
from flask import Flask
from flask import render_template, request
from . import backtracker
from . import kruskal


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

    backtracker_maze = backtracker.create_bactracker_maze(size)
    backtracker_image = backtracker.draw_maze_image(size, backtracker_maze)
    backtracker_impasses = backtracker.bactracker_maze_impasse_amount(backtracker_maze)

    kruskal_maze = kruskal.create_kruskal_maze(size)
    kruskal_image = kruskal.print_kruskal_maze(size, kruskal_maze)
    kruskal_impasses = kruskal.kruskal_maze_impasse_amount(kruskal_maze)

    return render_template("/results.html",
                           backtracker_maze=backtracker_maze,
                           backtracker_image=backtracker_image,
                           backtracker_impasses=backtracker_impasses,
                           kruskal_maze=kruskal_maze,
                           kruskal_image=kruskal_image,
                           kruskal_impasses=kruskal_impasses)


@app.route("/results")
def results():
    '''For results'''

    return render_template("/results.html")
