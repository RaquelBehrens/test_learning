import unittest
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To12X3, TestingShufflerPuzzleGame2x2To1X32
from src.puzzle_game import PuzzleGame

class CommandAndBranchCoverageTests(unittest.TestCase):

    def run_tests():
        unittest.main()

    # TEST CASE FOR [1-2(T)-3(T)-4]
    def test_direction_down_empty_in_bottom_border(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To12X3()
        shuffler.shuffle(puzzle_game)
        direction = "DOWN"
        # EXERCISE SUT
        result = puzzle_game.move_empty_tile(direction)
        # RESULT VERIFICATION
        self.assertFalse(result)

    # TEST CASE FOR [1-2(T)-3(F)-5-6]
    def test_direction_down_empty_not_in_bottom_border(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To1X32()
        shuffler.shuffle(puzzle_game)
        direction = "DOWN"
        # EXERCISE SUT
        result = puzzle_game.move_empty_tile(direction)
        # RESULT VERIFICATION
        self.assertTrue(result)

    # TEST CASE FOR [1-2(F)-7(T)-8(T)-9]
    def test_direction_up_empty_in_top_border(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To1X32()
        shuffler.shuffle(puzzle_game)
        direction = "UP"
        # EXERCISE SUT
        result = puzzle_game.move_empty_tile(direction)
        # RESULT VERIFICATION
        self.assertFalse(result)

    # TEST CASE FOR [1-2(F)-7(T)-8(F)-10-11]
    def test_direction_up_empty_not_in_top_border(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To12X3()
        shuffler.shuffle(puzzle_game)
        direction = "UP"
        # EXERCISE SUT
        result = puzzle_game.move_empty_tile(direction)
        # RESULT VERIFICATION
        self.assertTrue(result)

    # TEST CASE FOR [1-2(F)-7(F)-12(T)-13(T)-14]
    def test_direction_right_empty_in_right_border(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To1X32()
        shuffler.shuffle(puzzle_game)
        direction = "RIGHT"
        # EXERCISE SUT
        result = puzzle_game.move_empty_tile(direction)
        # RESULT VERIFICATION
        self.assertFalse(result)

    # TEST CASE FOR [1-2(F)-7(F)-12(T)-13(F)-15-16]
    def test_direction_right_empty_not_in_right_border(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To12X3()
        shuffler.shuffle(puzzle_game)
        direction = "RIGHT"
        # EXERCISE SUT
        result = puzzle_game.move_empty_tile(direction)
        # RESULT VERIFICATION
        self.assertTrue(result)

    # TEST CASE FOR [1-2(F)-7(F)-12(F)-17(T)-18(T)-19]
    def test_direction_left_empty_in_left_border(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To12X3()
        shuffler.shuffle(puzzle_game)
        direction = "LEFT"
        # EXERCISE SUT
        result = puzzle_game.move_empty_tile(direction)
        # RESULT VERIFICATION
        self.assertFalse(result)

    # TEST CASE FOR [1-2(F)-7(F)-12(F)-17(T)-18(F)-20-21]
    def test_direction_left_empty_not_in_left_border(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To1X32()
        shuffler.shuffle(puzzle_game)
        direction = "LEFT"
        # EXERCISE SUT
        result = puzzle_game.move_empty_tile(direction)
        # RESULT VERIFICATION
        self.assertTrue(result)

    # TEST CASE FOR [1-2(F)-7(F)-12(F)-17(F)]
    def test_with_invalid_direction(self):
        # INLINE FIXTURE SETUP
        puzzle_game = PuzzleGame(2)
        shuffler = TestingShufflerPuzzleGame2x2To1X32()
        shuffler.shuffle(puzzle_game)
        direction = "Invalid direction"
        # EXERCISE SUT
        result = puzzle_game.move_empty_tile(direction)
        # RESULT VERIFICATION
        self.assertIsNone(result)
