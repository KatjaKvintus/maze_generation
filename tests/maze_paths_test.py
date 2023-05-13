'''For testing the maze_paths.py file'''
import unittest
import random
from maze_generation import maze_paths, kruskal
from PIL import Image


class Test_maze_paths(unittest.TestCase):
    '''Kruskal's algoritm related tests'''



    def test_shortest_path_lenght_correct(self):
        '''Test to check that the shortest path will be found and
        the lenght is correct in size 4 maze.'''

        maze_4 = [[[1, 1, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0]],
                  [[1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 0]],
                  [[1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0]],
                  [[1, 1, 0, 1], [0, 0, 0, 1], [0, 0, 1, 1], [1, 0, 1, 1]]]
        
        path_lenght = maze_paths.shortest_path(maze_4)

        self.assertEqual(path_lenght, 10)


    def test_shortest_path_lenght_correct(self):
        '''Test to check that the shortest path will be found and
        the lenght is correct in size 5 maze.'''

        maze_5 = [[[1, 1, 0, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0]],
                  [[1, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0]],
                  [[1, 0, 0, 0], [0, 1, 1, 1], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 1]],
                  [[1, 0, 0, 0], [0, 1, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]],
                  [[1, 0, 1, 1], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]]
        
        path_lenght = maze_paths.shortest_path(maze_5)

        self.assertEqual(path_lenght, 8)



    def test_shortest_path_lenght_correct(self):
        '''Test to check that the shortest path will be found and
        the lenght is correct in size 10 maze.'''

        maze_10 = [[[1, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 
[[1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],
[[1, 1, 0, 0], [0, 1, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]],
[[1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]],
[[1, 1, 1, 0], [1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 1, 0]],
[[1, 0, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]],
[[1, 0, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 1], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 1]],
[[1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 1, 0]],
[[1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]],
[[1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [1, 1, 0, 1], [0, 0, 1, 1]]]
        
        path_lenght = maze_paths.shortest_path(maze_10)

        self.assertEqual(path_lenght, 50)


    def test_correct_return_if_no_path(self):
        '''Test to check that if there is no paths, the method will return -1.'''

        maze_5 = [[[1, 1, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0]],
                  [[1, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0]],
                  [[1, 0, 0, 0], [0, 1, 1, 1], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 1]],
                  [[1, 0, 0, 0], [0, 1, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]],
                  [[1, 0, 1, 1], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]]
        
        path_lenght = maze_paths.shortest_path(maze_5)

        self.assertEqual(path_lenght, -1)


    def test_shortest_path_of_three_when_a_is_shortest(self):
        '''Test to check that when given three different path lenghts (a, b, c),
        the program will found the shortest one. In this test case the shortest one
        is the a.'''

        test_sizes = []
        
        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)
        
        for size in test_sizes: 

            result = maze_paths.find_shortest_path_of_three(size, size+size, size*3)
            expected_phrase = "Iterative DFS maze with " + str(size) + " steps"

            self.assertEqual(result, expected_phrase)


    def test_shortest_path_of_three_when_b_is_shortest(self):
        '''Test to check that when given three different path lenghts (a, b, c),,
        the program will found the shortest one. In this test case the shortest one
        is b.'''

        test_sizes = []
        
        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)
        
        for size in test_sizes: 

            result = maze_paths.find_shortest_path_of_three(size+2, size, size*3)
            expected_phrase = "Kruskal's maze with " + str(size) + " steps"

            self.assertEqual(result, expected_phrase)


    def test_shortest_path_of_three_when_c_is_shortest(self):
        '''Test to check that when given three different path lenghts (a, b, c),,
        the program will found the shortest one. In this test case the shortest one
        is c.'''

        test_sizes = []
        
        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)
        
        for size in test_sizes: 

            result = maze_paths.find_shortest_path_of_three(size+2, size*4, size)
            expected_phrase = "Aldous-Broder maze with " + str(size) + " steps"

            self.assertEqual(result, expected_phrase)


    def test_shortest_path_of_three_when_a_and_b_are_equally_short(self):
        '''Test to check that when given three path lenghts (a, b, c), the program
        gives correct return when path a and b are the same length.'''

        test_sizes = []
        
        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)
        
        for size in test_sizes: 

            result = maze_paths.find_shortest_path_of_three(size, size, size + size)
            expected_phrase = "Iterative DFS maze and Kruskal's maze had equally short shortest path: " + str(size) + " steps"
            self.assertEqual(result, expected_phrase)


    def test_shortest_path_of_three_when_a_and_c_are_equally_short(self):
        '''Test to check that when given three path lenghts (a, b, c), the program
        gives correct return when path a and c are the same length.'''

        test_sizes = []
        
        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)
        
        for size in test_sizes: 

            result = maze_paths.find_shortest_path_of_three(size, size+size, size)
            expected_phrase = "Iterative DFS maze and Aldous-Broder maze had equally short shortest path: " + str(size) + " steps"
            self.assertEqual(result, expected_phrase)


    def test_shortest_path_of_three_when_b_and_c_are_equally_short(self):
        '''Test to check that when given three path lenghts (a, b, c), the program
        gives correct return when path b and c are the same length.'''

        test_sizes = []
        
        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)
        
        for size in test_sizes: 

            result = maze_paths.find_shortest_path_of_three(size+4, size, size)
            expected_phrase = "Kruskal's maze and Aldous-Broder maze had equally short shortest path: " + str(size) + " steps"
            self.assertEqual(result, expected_phrase)


    def test_shortest_path_function_notices_if_all_paths_have_same_leght(self):
        '''Test to check that when given three path lenghts, the program gives correct
        return when path 1 and 2 are the same length.'''

        test_sizes = []
        
        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)
        
        for size in test_sizes: 

            result = maze_paths.find_shortest_path_of_three(size, size, size)
            expected_phrase = "All mazes have equally short shortest path: " + str(size) + " steps"
            self.assertEqual(result, expected_phrase)


    def test_kruskal_maze_transformation_produces_correct_2D_lista(self):
        '''Test for checking that when kruskal maze (with edges list) is trasformed to
        the same format as DFS anf Andous-Broder mazes (2D list with each cell having a
        for digit binary list) the result is in correct form'''

        test_sizes = []

        for i in range (0, 5):
            i = random.randint(5, 200)
            test_sizes.append(i)

        for size in test_sizes:

            kruskal_maze = kruskal.create_kruskal_maze(size)
            transformed_maze = maze_paths.show_kruskal_maze_as_2_D_list(kruskal_maze)

            # Maze size should be size * size
            is_correct_size = size * size

            walls = 0
            doors = 0
            other_characters = 0

            # Maze should have only 1's for walls and 0's for doors, no other characters
            for row in transformed_maze:
                for cell in row:
                    for digit in cell:
                        if digit == 1:
                            walls += 1
                        elif digit == 0:
                            doors += 1
                        else:
                            other_characters += 1
            
            if walls > 0 and doors > 0 and other_characters == 0:
                has_both_doors_and_walls_and_not_other_characters = True
            else:
                has_both_doors_and_walls_and_not_other_characters = False

            self.assertEqual(len(transformed_maze) * size, is_correct_size)
            self.assertTrue(has_both_doors_and_walls_and_not_other_characters)


    def test_correct_response_when_all_maze_cells_not_reachable(self):
        '''Test to check if function are_all_cells_reachable() returns
        correctly 'False' if not all maze cells are reachable (= i or more cells
        has list [1, 1, 1, 1] meaning it is a closed room with no doors). '''

        maze = [[[1, 1, 0, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0]],
                  [[1, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0]],
                  [[1, 0, 0, 0], [0, 1, 1, 1], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 1]],
                  [[1, 0, 0, 0], [0, 1, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]],
                  [[1, 0, 1, 1], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 0, 1], [1, 1, 1, 1]]]
        
        result = maze_paths.are_all_cells_reachable(maze)
        self.assertFalse(result)


    def test_maze_type_is_correct_when_maze_is_perfect(self):
        '''Test to check that when function maze_type() is given a perfect maze
        as a parameter, it returns a correct phrase.'''

        maze = [[[1, 1, 0, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0]],
                  [[1, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0]],
                  [[1, 0, 0, 0], [0, 1, 1, 1], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 1]],
                  [[1, 0, 0, 0], [0, 1, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]],
                  [[1, 0, 1, 1], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]]

        result = maze_paths.maze_type(maze)
        self.assertEqual("perfect maze", result)


    def test_maze_type_is_correct_when_maze_is_not_perfect(self):
        '''Test to check that when function maze_type() is given a not-perfect maze
        as a parameter, it returns a correct phrase.'''

        maze = [[[1, 1, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0]],
                  [[1, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0]],
                  [[1, 0, 0, 0], [0, 1, 1, 1], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 1]],
                  [[1, 0, 0, 0], [0, 1, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]],
                  [[1, 0, 1, 1], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 0, 1], [1, 1, 1, 1]]]

        result = maze_paths.maze_type(maze)
        self.assertEqual("non-perfect maze", result)
        

