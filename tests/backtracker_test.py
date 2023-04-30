'''For testing the backtracker.py file'''
import unittest
import random
from maze_generation import backtracker


class Test_backtracker(unittest.TestCase):
    '''Bactracker related tests'''


    def test_maze_is_correct_size(self):
        '''Tests if the function creates a correct size 2D list.
        Test in 5 random integers between 5 and 50.'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 50)
            test_sizes.append(i)

        for size in test_sizes:

            self.new_maze = backtracker.create_bactracker_maze(size)
            maze_size = 0

            for row in self.new_maze:
                maze_size += len(row)

            self.assertEqual(maze_size, size*size)


    def test_maze_is_not_entirely_made_of_walls(self):
        '''Tests that that maze does contain open entryways too.
        Test in 5 random integers between 5 and 50.'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 50)
            test_sizes.append(i)

        for size in test_sizes:

            self.new_maze = backtracker.create_bactracker_maze(size)

            number_of_zeros = 0

            for row in self.new_maze:
                for item in row:
                    for character in item:
                        if character == 0:
                            number_of_zeros += 1

            self.assertGreater(number_of_zeros, 0)


    def test_maze_is_not_entirely_open_psaze(self):
        '''Tests that that maze does contain walls too.
        Test in 5 random integers between 5 and 50.'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 50)
            test_sizes.append(i)

        for size in test_sizes:
            self.new_maze = backtracker.create_bactracker_maze(size)

            number_of_walls = 0

            for row in self.new_maze:
                for item in row:
                    for character in item:
                        if character == 1:
                            number_of_walls += 1

            self.assertGreater(number_of_walls, 0)


    def test_maze_has_outer_frame(self):
        '''Tests that the maze has frame with no holes.
        Test in 20 random integers between 5 and 50.'''

        test_sizes = []

        for i in range (0, 20):
            i = random.randint(5, 50)
            test_sizes.append(i)

        for size in test_sizes:

            self.maze = backtracker.create_bactracker_maze(size)
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


    def test_impasse_method_works(self):
        '''For testing the maze_impasse_amount() method.
        It should always return an integer between 5 and 50^2.'''

        test_sizes = []

        for i in range (0, 20):
            i = random.randint(5, 50)
            test_sizes.append(i)

        for size in test_sizes:
            self.maze = backtracker.create_bactracker_maze(size)
            result = backtracker.bactracker_maze_impasse_amount(self.maze)
            self.assertTrue(0 <= result <= size*size)
