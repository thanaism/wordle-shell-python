import re
import random
import words


class Color:
    WHITE = "\33[37m"
    GREEN = "\033[32m"
    PURPLE = "\033[35m"
    END = "\033[0m"
    UP = "\033[1A"


class Game:
    def __init__(self):
        self.word_list = words.word_list
        self.solution = random.choice(self.word_list).upper()
        self.pattern = re.compile("[a-zA-Z]{5}")
        self.loop_count = 0
        self.is_correct = False
        self.current_word = ""

    def check_input(self):
        s = self.current_word
        n = len(s)
        if n < 5:
            print(s.upper() + " is too short.")
            return False
        if n > 5:
            print(s.upper() + " is too long.")
            return False
        if not self.pattern.match(s):
            print(s.upper() + " is non-alphabetic.")
            return False
        if s.lower() not in self.word_list:
            print(s.upper() + " is not in word list.")
            return False
        return True

    def judge(self):
        s = self.current_word.upper()
        output = ""
        ok_count = 0
        for i in range(5):
            if s[i] == self.solution[i]:
                output += Color.GREEN + s[i]
                ok_count += 1
            elif s[i] in self.solution:
                output += Color.PURPLE + s[i]
            else:
                output += Color.WHITE + s[i]
        output += Color.END
        print(output)
        return ok_count == 5


def main():
    game = Game()
    while True:
        if game.loop_count == 6:
            if game.is_correct:
                print("Genius!")
            else:
                print("Try again.")
            break

        game.current_word = input()

        print(Color.UP, end="")
        if not game.check_input():
            continue

        game.loop_count += 1

        if game.judge():
            game.is_correct = True


if __name__ == "__main__":
    main()
