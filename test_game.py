import unittest


import unittest
import wordle


class TestGame(unittest.TestCase):
    def test_check_input(self):
        game = wordle.Game()
        game.current_word = "think"
        self.assertTrue(game.check_input())
        game.current_word = "ANGLE"
        self.assertTrue(game.check_input())
        game.current_word = "HOLT"
        self.assertFalse(game.check_input())
        game.current_word = "BEAUTIFUL"
        self.assertFalse(game.check_input())
        game.current_word = "ET+AL"
        self.assertFalse(game.check_input())

    def test_judge(self):
        game = wordle.Game()
        game.solution = "ANGLE"
        game.current_word = "ANGLE"
        self.assertTrue(game.judge())
        game.solution = "ANGLE"
        game.current_word = "THINK"
        self.assertFalse(game.judge())


if __name__ == "__main__":
    unittest.main()
