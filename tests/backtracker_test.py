import unittest
from backtracker import backtracker


class Test_backtracker(unittest.TestCase):


    def test_maze_is_correct_size(self):
        self.new_maze = create_bactracker_maze(4)
        maze_size = 4 * 4
        self.assertEqual(len(self.new_maze), maze_size)
    

    def test_maze_is_not_entirely_made_of_walls(self):
        self.new_maze = create_bactracker_maze(4)

        number_of_zeros = 0

        for row in maze:
            for item in row:
                for character in item:
                    if character == 0:
                        number_of_zeros += 1
        
        self.assertGreater(number_of_zeros, 0)
        
        