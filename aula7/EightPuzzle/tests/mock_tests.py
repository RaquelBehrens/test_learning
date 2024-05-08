import unittest
from unittest.mock import patch
from src.puzzle_game import PuzzleGame
from src.puzzle_game_with_mock import PuzzleGameWithPlayer
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To12X3

class MockTests(unittest.TestCase):

    def run_tests():
        unittest.main()

    def setUp(self):
        # IMPLICIT FIXTURE SETUP
        self.puzzle_game = PuzzleGame(2)
        self.puzzle_game_with_player = PuzzleGameWithPlayer(2, 'Raquel')
        shuffler = TestingShufflerPuzzleGame2x2To12X3()
        shuffler.shuffle(self.puzzle_game)
        shuffler.shuffle(self.puzzle_game_with_player)
        # 1  2
        # -  3

        # Game finished would be:
        # 1  2
        # 3  -

    def test_change_tiles_1_1_and_2_1_in_puzzle_game_2x2_without_mock(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        self.puzzle_game.move_empty_tile("UP")
        # RESULT VERIFICATION: 
        self.assertEqual(' ', self.puzzle_game.get_tile(1, 1))
        self.assertEqual(1, self.puzzle_game.get_tile(2, 1)) 
        self.assertEqual(2, self.puzzle_game.get_tile(1, 2)) 
        self.assertEqual(3, self.puzzle_game.get_tile(2, 2)) 

    @patch('src.puzzle_game.PuzzleGame.get_tile')
    def test_change_tiles_1_1_and_2_1_in_puzzle_game_2x2_with_mock(self, mock_puzzle_game_get_tile):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        self.puzzle_game.move_empty_tile("UP")
        # RESULT VERIFICATION: 
        mock_puzzle_game_get_tile.return_value = ' '
        self.assertEqual(' ', self.puzzle_game.get_tile(1, 1))
        mock_puzzle_game_get_tile.return_value = 1
        self.assertEqual(1, self.puzzle_game.get_tile(2, 1))
        mock_puzzle_game_get_tile.return_value = 2
        self.assertEqual(2, self.puzzle_game.get_tile(1, 2))
        mock_puzzle_game_get_tile.return_value = 3
        self.assertEqual(3, self.puzzle_game.get_tile(2, 2))

    def test_change_tiles_2_2_and_1_2_in_puzzle_game_2x2_without_mock(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        self.puzzle_game.move_empty_tile("RIGHT")
        # RESULT VERIFICATION: 
        self.assertEqual(1, self.puzzle_game.get_tile(1, 1))
        self.assertEqual(3, self.puzzle_game.get_tile(2, 1)) 
        self.assertEqual(2, self.puzzle_game.get_tile(1, 2)) 
        self.assertEqual(' ', self.puzzle_game.get_tile(2, 2)) 

    @patch('src.puzzle_game.PuzzleGame.get_tile')
    def test_change_tiles_2_2_and_1_2_in_puzzle_game_2x2_with_mock(self, mock_puzzle_game_get_tile):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        self.puzzle_game.move_empty_tile("RIGHT")
        # RESULT VERIFICATION: 
        mock_puzzle_game_get_tile.return_value = 1
        self.assertEqual(1, self.puzzle_game.get_tile(1, 1))
        mock_puzzle_game_get_tile.return_value = 3
        self.assertEqual(3, self.puzzle_game.get_tile(2, 1))
        mock_puzzle_game_get_tile.return_value = 2
        self.assertEqual(2, self.puzzle_game.get_tile(1, 2))
        mock_puzzle_game_get_tile.return_value = ' '
        self.assertEqual(' ', self.puzzle_game.get_tile(2, 2))

    def test_end_of_the_game_true_without_mock(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUPpuzzleGame
        # EXERCISE SUT
        self.puzzle_game_with_player.move_tile_from_a_position_to_the_empty_position(2, 2)
        finished = PuzzleGameWithPlayer.end_of_the_game(self.puzzle_game_with_player)
        # RESULT VERIFICATION: 
        self.assertEqual("Saved", finished)

    def test_end_of_the_game_false_without_mock(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        finished = PuzzleGameWithPlayer.end_of_the_game(self.puzzle_game_with_player)
        # RESULT VERIFICATION: 
        self.assertEqual('Game not finished', finished)

    @patch('src.puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_the_game_true_with_mock(self, mock_puzzle_game_with_mock_save_game_to_file):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        self.puzzle_game_with_player.move_tile_from_a_position_to_the_empty_position(2, 2)
        mock_puzzle_game_with_mock_save_game_to_file.return_value = "Saved"
        finished = PuzzleGameWithPlayer.end_of_the_game(self.puzzle_game_with_player)
        # RESULT VERIFICATION: 
        self.assertTrue("Saved", finished)

    @patch('src.puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_the_game_true_with_mock_2(self, mock_puzzle_game_with_mock_save_game_to_file):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        self.puzzle_game_with_player.move_tile(3)
        mock_puzzle_game_with_mock_save_game_to_file.return_value = "Saved"
        finished = PuzzleGameWithPlayer.end_of_the_game(self.puzzle_game_with_player)
        # RESULT VERIFICATION: 
        self.assertTrue("Saved", finished)

    @patch('src.puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_the_game_false_with_mock(self, mock_puzzle_game_with_mock_save_game_to_file):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        mock_puzzle_game_with_mock_save_game_to_file.return_value = "Saved"
        finished = PuzzleGameWithPlayer.end_of_the_game(self.puzzle_game_with_player)
        # RESULT VERIFICATION: 
        self.assertEqual('Game not finished', finished)