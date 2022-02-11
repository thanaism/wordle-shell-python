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

    def test_gen_ouput(self):
        game = wordle.Game()

        W = wordle.Color.WHITE
        P = wordle.Color.PURPLE
        G = wordle.Color.GREEN

        game.solution = "AAAAA"
        game.current_word = "ABBBB"
        output, ok_count = game.gen_output()
        self.assertTrue(output.count(W) == 4)
        self.assertTrue(output.count(P) == 0)
        self.assertTrue(output.count(G) == 1)
        self.assertEqual(ok_count, 1)

        game.solution = "ABCDE"
        game.current_word = "EDCBA"
        output, ok_count = game.gen_output()
        self.assertTrue(output.count(W) == 0)
        self.assertTrue(output.count(P) == 4)
        self.assertTrue(output.count(G) == 1)
        self.assertEqual(ok_count, 1)

        game.solution = "ABCDE"
        game.current_word = "ABCDE"
        output, ok_count = game.gen_output()
        self.assertTrue(output.count(W) == 0)
        self.assertTrue(output.count(P) == 0)
        self.assertTrue(output.count(G) == 5)
        self.assertEqual(ok_count, 5)

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
