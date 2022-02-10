import re
import random
import words

word_list = words.word_list
solution = random.choice(word_list).upper()
pattern = re.compile("[a-zA-Z]{5}")
loop_count = 0
is_correct = False


class Color:
    WHITE = "\33[37m"
    GREEN = "\033[32m"
    PURPLE = "\033[35m"
    END = "\033[0m"
    UP = "\033[1A"


def check_input(s):
    n = len(s)
    print(Color.UP, end="")
    if n < 5:
        print(s.upper() + " is too short.")
        return False
    if n > 5:
        print(s.upper() + " is too long.")
        return False
    if not pattern.match(s):
        print(s.upper() + " is non-alphabetic.")
        return False
    if s.lower() not in word_list:
        print(s.upper() + " is not in word list.")
        return False
    return True


def judge(s):
    output = ""
    ok_count = 0
    for i in range(5):
        if s[i] == solution[i]:
            output += Color.GREEN + s[i]
            ok_count += 1
        elif s[i] in solution:
            output += Color.PURPLE + s[i]
        else:
            output += Color.WHITE + s[i]
    output += Color.END
    print(output)
    return ok_count == 5


while True:
    if loop_count == 6:
        if is_correct:
            print("Genius!")
        else:
            print("Try again.")
        break

    s = input()

    if not check_input(s):
        continue

    loop_count += 1

    if judge(s.upper()):
        is_correct = True
