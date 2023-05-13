'''For testing the dfs.py file'''
import unittest
import random
from maze_generation import maze_tools, maze_paths, dfs
from PIL import Image


class Test_dfs(unittest.TestCase):
    '''Bactracker related tests'''


    def test_maze_is_correct_size(self):
        '''Tests if the function creates a correct size dfs maze  (=2D list).
        Test in 5 random integers between 5 and 200.'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:

            self.new_maze = dfs.create_dfs_maze(size)
            maze_size = 0

            for row in self.new_maze:
                maze_size += len(row)

            self.assertEqual(maze_size, size*size)


    def test_too_small_parameter_gives_error(self):
        '''Test that when trying to generate a dfs maze any integer smaller
        than 4 returns error'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(-10, 3)
            test_sizes.append(i)

        for size in test_sizes:
            result = dfs.create_dfs_maze(size)
            self.assertEqual(result, "Too small parameter")


    def test_too_big_parameter_gives_error(self):
        '''Test that when trying to generate a dfs maze any integer bigger
        than 200 returns error'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(201, 1000)
            test_sizes.append(i)

        for size in test_sizes:
            result = dfs.create_dfs_maze(size)
            self.assertEqual(result, "Too big parameter")


    def test_incorrect_parameter_type_gives_error(self):
        '''If create_fds_maze() has a wrong type of parameter, it
        returns an error'''

        test_types = ["kissa", "#", 4.44]

        for item in test_types:

            result = dfs.create_dfs_maze(item)
            self.assertEqual(result, "Incorrect parameter type")


    def test_maze_is_not_entirely_made_of_walls(self):
        '''Tests that that dfs maze does contain open entryways (doors) too. Wall = 1,
        door = 0. Test in 5 random integers between 5 and 200.'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:

            self.new_maze = dfs.create_dfs_maze(size)

            number_of_zeros = 0

            for row in self.new_maze:
                for item in row:
                    for character in item:
                        if character == 0:
                            number_of_zeros += 1

            self.assertGreater(number_of_zeros, 0)


    def test_maze_is_not_entirely_open_space(self):
        '''Tests that that dfs maze does contain walls too. Wall = 1,
        door = 0. Tests in 5 random integers between 5 and 200.'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:
            self.new_maze = dfs.create_dfs_maze(size)

            number_of_walls = 0

            for row in self.new_maze:
                for item in row:
                    for character in item:
                        if character == 1:
                            number_of_walls += 1

            self.assertGreater(number_of_walls, 0)


    def test_maze_has_outer_frame(self):
        '''Tests that the dfs maze has frame with no holes (doors). Wall = 1,
        door = 0. Test in 20 random integers between 5 and 200.'''

        test_sizes = []

        for i in range (0, 20):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:

            self.maze = dfs.create_dfs_maze(size)
            frame_is_unbroken = True
            i = 0
            j = 0

            while i < size:
                while j < size:

                    if i == 0:
                        if self.maze[i][j][1] != 1:
                            frame_is_unbroken = False

                    if i == size - 1:
                        if self.maze[i][j][3] != 1:
                            frame_is_unbroken = False

                    if j == 0:
                        if self.maze[i][j][0] != 1:
                            frame_is_unbroken = False

                    if j== size - 1:
                        if self.maze[i][j][2] != 1:
                            frame_is_unbroken = False

                    j += 1
                i += 1

            self.assertTrue(frame_is_unbroken)


    def test_impasse_method_returns_integer_in_correct_size(self):
        '''For testing the dfs maze impasses. It should always return
        an integer between 0 and 200^2.'''

        test_sizes = []

        for i in range (0, 20):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:
            self.maze = dfs.create_dfs_maze(size)
            result = maze_tools.count_maze_impasses(self.maze)
            self.assertTrue(0 <= result <= size*size)
    

    def test_impasses_are_counted_correctly_in_size_4_maze(self):
        '''For checking that impasses in 4x4 dfs maze are count correctly'''

        maze_4 = [[[1, 1, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0]],
                  [[1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 0]],
                  [[1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0]],
                  [[1, 1, 0, 1], [0, 0, 0, 1], [0, 0, 1, 1], [1, 0, 1, 1]]]
        
        result = maze_tools.count_maze_impasses(maze_4)
        self.assertEqual(result, 4)
    

    def test_impasses_are_counted_correctly_in_size_5_maze(self):
        '''For checking that impasses in 5x5 dfs maze are count correctly'''

        maze_5 = [[[1, 1, 0, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0]],
                  [[1, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0]],
                  [[1, 0, 0, 0], [0, 1, 1, 1], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 1]],
                  [[1, 0, 0, 0], [0, 1, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]],
                  [[1, 0, 1, 1], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]]
        
        result = maze_tools.count_maze_impasses(maze_5)
        self.assertEqual(result, 6)


    def test_is_this_perfect_maze(self):
        '''Checks if all dfs maze cells can be reached from every other cell'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:

            self.new_maze = dfs.create_dfs_maze(size)            
            result = maze_paths.are_all_cells_reachable(self.new_maze)

            self.assertTrue(result)
    

    def test_shortest_path_is_under_max_length(self):
        '''Test to check that the shortest path can be found in dfs maze
        and its length is not bigger than matrix cells amount.'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:

            max_size = size * size
            maze = dfs.create_dfs_maze(size)
            path_length = maze_paths.shortest_path(maze)
            self.assertLessEqual(path_length, max_size)
    

    def test_shortest_path_is_at_least_minimum_length(self):
        '''Test to check that the shortest path can be found in dfs maze
        and its length is not shorter than the mimimum path length
        in matrix (= size + size - 2).'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:

            min_size = size + size - 2
            maze = dfs.create_dfs_maze(size)
            path_length = maze_paths.shortest_path(maze)
            self.assertGreaterEqual(path_length, min_size)
