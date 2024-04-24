import unittest
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To12X3
from src.invalid_position_exception import InvalidPositionException
from src.puzzle_game import PuzzleGame

class DataFlowTests(unittest.TestCase):

    def run_tests():
        unittest.main()

    def setUp(self):
        # IMPLICIT FIXTURE SETUP
        self.puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To12X3()
        # 1  2
        # -  3
        shuffler.shuffle(self.puzzle_game)

    # TEST CASE TO KILL MUTANT 36
    def test_case_move_tile_from_a_position_to_the_empty_position_mut_36(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        line = 1
        column = 1  
         # EXERCISE SUT
        result = self.puzzle_game.move_tile_from_a_position_to_the_empty_position(line, column)  
        # RESULT VERIFICATION: 
        self.assertTrue(result)

    # TEST CASE TO KILL MUTANT 37
    def test_case_move_tile_from_a_position_to_the_empty_position_mut_37(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        line = 1
        column = 2 
         # EXERCISE SUT
        result = self.puzzle_game.move_tile_from_a_position_to_the_empty_position(line, column)  
        # RESULT VERIFICATION: 
        self.assertFalse(result)

    # TEST CASE FOR ALL P-USES OF LINE AND COLUMN: 1-2-3-4
    def test_case_1_2_3_4(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        line = 2
        column = 1
        excpected_result = ' ' #tile in line 2, column 1 is empty, should return empty
        # EXERCISE SUT
        result = self.puzzle_game.get_tile(line, column)
        # RESULT VERIFICATION: 
        self.assertEqual(result, excpected_result)

    # TEST CASE TO KILL MUTANT 98
    def test_case_1_2_3_4_mut_98(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        line = 0
        column = 1    
        # RESULT VERIFICATION: 
        with self.assertRaises(InvalidPositionException):
            # EXERCISE SUT
            result = self.puzzle_game.get_tile(line, column)

    # TEST CASE TO KILL MUTANT 101
    def test_case_1_2_3_4_mut_101(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        line = 1
        column = 0    
        # RESULT VERIFICATION: 
        with self.assertRaises(InvalidPositionException):
            # EXERCISE SUT
            result = self.puzzle_game.get_tile(line, column)

    # TEST CASE FOR ALL C-USES OF LINE AND COLUMN: 1-2-3-5
    # AND
    # TEST CASE FOR ALL P-USES OF LINE AND COLUMN: 1-2-3-5
    def test_case_1_2_3_5(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        line = 1
        column = 2
        excpected_result = 2 #tile in line 1, column 2 is 2
        # EXERCISE SUT
        result = self.puzzle_game.get_tile(line, column)
        # RESULT VERIFICATION
        self.assertEqual(result, excpected_result)

    # TEST CASE TO KILL MUTANT 107
    def test_case_1_2_3_5_mut_107(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        line = 2
        column = 2
        excpected_result = 3 #tile in line 1, column 2 is 2
        # EXERCISE SUT
        result = self.puzzle_game.get_tile(line, column)
        # RESULT VERIFICATION
        self.assertEqual(result, excpected_result)


    # TEST CASE FOR ALL P-USES OF LINE AND COLUMN: 1-2-6
    def test_case_1_2_6(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        line = 1
        column = 3
        # RESULT VERIFICATION
        with self.assertRaises(InvalidPositionException):
            # EXERCISE SUT
            self.puzzle_game.get_tile(line, column)