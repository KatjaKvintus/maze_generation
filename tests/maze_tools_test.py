'''For testing the maze_tools.py file'''
import unittest
import random
from maze_generation import aldous_broder, backtracker, kruskal, maze_paths
from PIL import Image
import os


class Test_maze_tools(unittest.TestCase):
    '''maze_tools.py related tests'''


    def test_drawing_function_returns_file_that_is_not_empty(self):
        """Checks that the function return file is file and not empty"""

        size = random.randint(4, 20)
        test_algorithms = ["aldous_broder", "backtracker", "kruskal"]

        for algorithm in test_algorithms:

            if algorithm == "backtracker":

                self.backtracker_maze = backtracker.create_bactracker_maze(size)
                self.maze_image = backtracker.draw_maze_image(size, self.backtracker_maze)
                self.maze_image = "static/backtracker_maze_image.jpg"

                self.assertTrue(os.path.isfile(self.maze_image))
                self.assertGreater(os.path.getsize(self.maze_image), 0)
            
            elif algorithm == "kruskal":

                self.kruskal_maze = kruskal.create_kruskal_maze(size)
                self.maze_image = kruskal.print_kruskal_maze(size, self.kruskal_maze)
                self.maze_image = "static/kruskal_maze_image.jpg"

                self.assertTrue(os.path.isfile(self.maze_image))
                self.assertGreater(os.path.getsize(self.maze_image), 0)

            elif algorithm == "aldous_broder":

                self.aldous_broder_maze = aldous_broder.create_aldous_broder_maze(size) 
                self.maze_image = aldous_broder.draw_aldous_broder_maze_image(size, self.aldous_broder_maze)          
                self.maze_image = "static/aldous_broder_maze_image.jpg"

                self.assertTrue(os.path.isfile(self.maze_image))
                self.assertGreater(os.path.getsize(self.maze_image), 0)
