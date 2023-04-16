'''For testing the kruskal.py file'''
import unittest
import random
from . import kruskal


class Test_kruskal(unittest.TestCase):
    '''Kruskal's algoritm related tests'''


    def test_maze_is_correct_size(self):
        '''Tests if the function creates a correct size 2D list.
        Test in 5 random integers between 5 and 50.'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 50)
            test_sizes.append(i)

        for size in test_sizes:

            self.new_maze = kruskal.create_kruskal_maze(size)
            maze_size = 0

            for row in self.new_maze:
                maze_size += len(row)

            self.assertEqual(maze_size, size*size)


    def test_maze_has_open_edges(self):
        '''Tests that that maze does contain open entryways too.
        Each cell should have more than 0 open edges listed in
        the open_edges list.
        Test in 5 random integers between 5 and 50.'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 50)
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
            i = random.randint(5, 50)
            test_sizes.append(i)

        for size in test_sizes:

            self.new_maze = kruskal.create_kruskal_maze(size)

            number_of_odd_amount_of_edges = 0

            for row in self.new_maze:
                for cell in row:
                    if len(cell.open_edges)%2 != 0:
                        number_of_odd_amount_of_edges += 1

            self.assertEqual(number_of_odd_amount_of_edges, 0)


    '''
    def test_return_type_for_get_open_edges(self):
        '''

'''
        Checks that function get_open_edges() returns
        a list.
        Note: this method fails because it is in class Cell
        inside kruskal.py and I don't know how to refer to it.'''
'''
        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 50)
            test_sizes.append(i)

        for size in test_sizes:
            self.new_maze = kruskal.create_kruskal_maze(size)

            for cell in self.new_maze:
                result = kruskal.get_open_edges(cell)
                self.assertTrue(isinstance(result, list))
'''
