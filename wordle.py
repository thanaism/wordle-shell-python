import re
import random
import words
from typing import TypeVar, Tuple

TGame = TypeVar("TGame", bound="Game")


class Color:
    WHITE = "\33[37m"
    GREEN = "\033[32m"
    PURPLE = "\033[35m"
    END = "\033[0m"
    UP = "\033[1A"


class Game:
    def __init__(self: TGame) -> None:
        self._word_list = words.word_list
        self._solution = random.choice(self._word_list).upper()
        self._pattern = re.compile("[a-zA-Z]{5}")
        self._loop_count = 0
        self._is_correct = False
        self._current_word = ""

    def check_input(self: TGame) -> bool:
        s = self._current_word
        n = len(s)
        if n < 5:
            print(s.upper() + " is too short.")
            return False
        if n > 5:
            print(s.upper() + " is too long.")
            return False
        if not self._pattern.match(s):
            print(s.upper() + " is non-alphabetic.")
            return False
        if s.lower() not in self._word_list:
            print(s.upper() + " is not in word list.")
            return False
        return True

    def judge(self: TGame) -> bool:
        output, ok_count = self.gen_output()
        print(output)
        return ok_count == 5

    def gen_output(self: TGame) -> Tuple[str, int]:
        s = self._current_word.upper()
        output = ""
        ok_count = 0
        for i in range(5):
            if s[i] == self._solution[i]:
                output += Color.GREEN + s[i]
                ok_count += 1
            elif s[i] in self._solution:
                output += Color.PURPLE + s[i]
            else:
                output += Color.WHITE + s[i]
        output += Color.END
        return output, ok_count

    def run(self: TGame) -> bool:
        while True:
            if self._loop_count == 6:
                if self._is_correct:
                    print("Genius!")
                    return True
                else:
                    print("Try again.")
                    return False

            self._current_word = input()

            print(Color.UP, end="")
            if not self.check_input():
                continue

            self._loop_count += 1

            if self.judge():
                self._is_correct = True


def main() -> None:
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
