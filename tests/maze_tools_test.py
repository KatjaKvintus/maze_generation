'''For testing the maze_tools.py file'''
import unittest
import random
from maze_generation import dfs, aldous_broder, kruskal, maze_paths, maze_tools
from PIL import Image
import os
import time


class Test_maze_tools(unittest.TestCase):
    '''maze_tools.py related tests'''


    def test_drawing_function_returns_file_that_is_not_empty(self):
        """Checks that the function return file is file and not empty"""

        size = random.randint(4, 20)
        test_algorithms = ["aldous_broder", "dfs", "kruskal"]

        for algorithm in test_algorithms:

            if algorithm == "dfs":

                self.dfs_maze = dfs.create_dfs_maze(size)
                self.maze_image = dfs.draw_maze_image(size, self.dfs_maze)
                self.maze_image = "static/dfs_maze_image.jpg"

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
    


    def test_fastest_maze_generation_algorithm_function(self):
        '''test for fastest_maze_generation_algorithm() function'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(-10, 3)
            test_sizes.append(i)

        for size in test_sizes:

            # DFS algorithm
            start_time = time.time()
            dfs_maze = dfs.create_dfs_maze(size)
            end_time = time.time()
            dfs_execution_time = round((end_time - start_time) * 1000, 4)
            
            # Kruskal's algorithm
            start_time = time.time()
            kruskal_maze = kruskal.create_kruskal_maze(size)
            end_time = time.time()
            kruskal_execution_time = round((end_time - start_time) * 1000, 4)
            
            # Aldous-Broder algorithm
            start_time = time.time()
            aldous_broder_maze = aldous_broder.create_aldous_broder_maze(size)
            end_time = time.time()
            aldous_broder_execution_time = round((end_time - start_time) * 1000, 4)

            fastest_time = min(dfs_execution_time, kruskal_execution_time,
                               aldous_broder_execution_time)
            
            if dfs_execution_time < kruskal_execution_time and dfs_execution_time < aldous_broder_execution_time:
                function_return = "Iterative DFS algorithm in " + str(dfs_execution_time) + " ms"
                
            elif kruskal_execution_time < dfs_execution_time and kruskal_execution_time < aldous_broder_execution_time:
                function_return = "Kruskal's algorithm in " + str(kruskal_execution_time) + " ms"
            else:
                function_return = "Aldous-Broder algorithm in " + str(aldous_broder_execution_time) + " ms"
            
            result = maze_tools.fastest_maze_generation_algorithm(dfs_execution_time, 
                                                    kruskal_execution_time,
                                                    aldous_broder_execution_time)
            
            self.assertEqual(result, function_return)
            

