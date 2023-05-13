'''For testing the kruskal.py file'''
import unittest
import random
from maze_generation import kruskal, maze_paths
from PIL import Image


class Test_kruskal(unittest.TestCase):
    '''Kruskal's algoritm related tests'''


    def test_maze_is_correct_size(self):
        '''Tests if the create_kruskal_maze() function creates
        a correct size 2D list. Test in 5 random integers between
        5 and 200.'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:

            self.new_maze = kruskal.create_kruskal_maze(size)
            maze_size = 0

            for row in self.new_maze:
                maze_size += len(row)

            self.assertEqual(maze_size, size*size)


    def test_too_small_parameter_gives_error(self):
        '''Test that when trying to generate a Kurskal maze any integer smaller
        than 4 returns error'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(-10, 3)
            test_sizes.append(i)

        for size in test_sizes:
            result = kruskal.create_kruskal_maze(size)
            self.assertEqual(result, "Too small parameter")


    def test_too_big_parameter_gives_error(self):
        '''Test that when trying to generate a Kurskal maze any integer bigger
        than 200 returns error'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(201, 1000)
            test_sizes.append(i)

        for size in test_sizes:
            result = kruskal.create_kruskal_maze(size)
            self.assertEqual(result, "Too big parameter")


    def test_incorrect_parameter_type_gives_error(self):
        ''' If create_kruskal_maze() has a wrong type of parameter,
        there will be error'''

        test_types = ["Harry Potter", "?", 12.3]

        for item in test_types:

            result = kruskal.create_kruskal_maze(item)
            self.assertEqual(result, "Incorrect parameter type")



    def test_maze_has_open_edges(self):
        '''Tests that that Kurskal maze does contain open entryways too.
        Each cell should have more than 0 open edges listed in
        the open_edges list. Tests in 5 random integers between 5 and 200.'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:

            self.new_maze = kruskal.create_kruskal_maze(size)

            number_of_zeros = 0

            for row in self.new_maze:
                for cell in row:
                    if len(cell.open_edges) < 1:
                        number_of_zeros += 1

            self.assertEqual(number_of_zeros, 0)


    def test_open_edges_always_in_pairs(self):
        '''When opening an edge it will be opened for both ways ->
        open edges are always added to open_edges list in pairs
        (a->b and b->a). This checks that each open_edges list
        has an even number of edges. '''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:

            self.new_maze = kruskal.create_kruskal_maze(size)

            number_of_odd_amount_of_edges = 0

            for row in self.new_maze:
                for cell in row:
                    if len(cell.open_edges)%2 != 0:
                        number_of_odd_amount_of_edges += 1

            self.assertEqual(number_of_odd_amount_of_edges, 0)


    def test_shortest_path_is_under_max_length(self):
        '''Test to check that the shortest path in Kurskal maze can be found
        and its length is not bigger than matrix cells amount.'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:

            max_size = size * size
            maze = kruskal.create_kruskal_maze(size)
            maze_modified = maze_paths.show_kruskal_maze_as_2_D_list(maze)
            path_length = maze_paths.shortest_path(maze_modified)
            self.assertLessEqual(path_length, max_size)


    def test_shortest_path_is_at_least_minimum_length(self):
        '''Test to check that the shortest path can be found
        and its length is not shorter than the mimimum path length
        in matrix = size + size - 2.'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:

            min_size = size + size - 2
            maze = kruskal.create_kruskal_maze(size)
            maze_modified = maze_paths.show_kruskal_maze_as_2_D_list(maze)
            path_length = maze_paths.shortest_path(maze_modified)
            self.assertGreaterEqual(path_length, min_size)
