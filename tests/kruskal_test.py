'''For testing the kruskal.py file'''
import unittest
import random
from maze_generation import kruskal
from PIL import Image


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


    def test_too_small_parameter_gives_error(self):
        '''Test that when trying to generate a maze any integer smaller
        than 4 returns error'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(-10, 3)
            test_sizes.append(i)

        for size in test_sizes:
            result = kruskal.create_kruskal_maze(size)
            self.assertEqual(result, "Too small parameter")
    
 
    def test_too_big_parameter_gives_error(self):
        '''Test that when trying to generate a maze any integer bigger
        than 200 returns error'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(201, 1000)
            test_sizes.append(i)

        for size in test_sizes:
            result = kruskal.create_kruskal_maze(size)
            self.assertEqual(result, "Too big parameter")


    def test_incorrect_parameter_type_gives_error(self):
        ''' If create_bactracker_maze() has a wrong type of parameter,
        there will be error'''

        test_types = ["Harry Potter", "?", 12.3]

        for item in test_types:

            result = kruskal.create_kruskal_maze(item)
            self.assertEqual(result, "Incorrect parameter type")



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
