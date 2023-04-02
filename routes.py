'''Routes for webapp pages and functionalities'''
from app import app
from flask import render_template, request


@app.route("/", methods=["GET", "POST"])
def index():
    '''Route: index.html'''
    return render_template("index.html")


@app.route("/choose_algorithms", methods=["GET"])
def choose_algorithms():
    '''Handles users choices of algorithms for comparison'''

    if request.method == "POST":
        algorithm_1 = request.form["algorithm_1"]
        algorithm_2 = request.form["algorithm_2"]
        maze_size = request.form["maze_size"]

    return render_template("/generate_maze",
                            algorithm_1=algorithm_1,
                            algorithm_2=algorithm_2,
                            maze_size=maze_size)


@app.route("/generate_maze")
def generate_maze():
    '''For maze calls'''

    # Sokkeloita luovien ja visualisoivien funktioiden kutsuminen tänne

    return render_template("/results")


@app.route("/results")
def results():
    '''For results'''

    # Tulosten muotoilu tänne

    return render_template("/results.html")
