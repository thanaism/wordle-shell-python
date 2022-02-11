import unittest
import wordle


class TestGame(unittest.TestCase):
    def test_check_input(self):
        game = wordle.Game()

        game._current_word = "think"
        self.assertTrue(game.check_input())

        game._current_word = "ANGLE"
        self.assertTrue(game.check_input())

        game._current_word = "HOLT"
        self.assertFalse(game.check_input())

        game._current_word = "BEAUTIFUL"
        self.assertFalse(game.check_input())

        game._current_word = "ET+AL"
        self.assertFalse(game.check_input())

    def test_gen_ouput(self):
        game = wordle.Game()

        W = wordle.Color.WHITE
        P = wordle.Color.PURPLE
        G = wordle.Color.GREEN

        game._solution = "AAAAA"
        game._current_word = "ABBBB"
        output, ok_count = game.gen_output()
        self.assertTrue(output.count(W) == 4)
        self.assertTrue(output.count(P) == 0)
        self.assertTrue(output.count(G) == 1)
        self.assertEqual(ok_count, 1)

        game._solution = "ABCDE"
        game._current_word = "EDCBA"
        output, ok_count = game.gen_output()
        self.assertTrue(output.count(W) == 0)
        self.assertTrue(output.count(P) == 4)
        self.assertTrue(output.count(G) == 1)
        self.assertEqual(ok_count, 1)

        game._solution = "ABCDE"
        game._current_word = "ABCDE"
        output, ok_count = game.gen_output()
        self.assertTrue(output.count(W) == 0)
        self.assertTrue(output.count(P) == 0)
        self.assertTrue(output.count(G) == 5)
        self.assertEqual(ok_count, 5)

    def test_judge(self):
        game = wordle.Game()

        game._solution = "ANGLE"
        game._current_word = "ANGLE"
        self.assertTrue(game.judge())

        game._solution = "ANGLE"
        game._current_word = "THINK"
        self.assertFalse(game.judge())

    def test_run(self):
        game = wordle.Game()

        game._loop_count = 6

        game._is_correct = True
        self.assertTrue(game.run())

        game._is_correct = False
        self.assertFalse(game.run())


if __name__ == "__main__":
    unittest.main()
