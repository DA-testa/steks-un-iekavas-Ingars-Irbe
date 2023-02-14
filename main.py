# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text: str):
    opening_brackets_stack = []

    for i, next in enumerate(text):

        if next in "([{":
            opening_brackets_stack.append(next)

        if next in ")]}":
            rightB = Bracket(next, i+1)

            if opening_brackets_stack == [] or not are_matching(opening_brackets_stack.pop(), next):
                return rightB.position 
            
    if opening_brackets_stack:
        return rightB.position
    else:
        return 0

def main():
    text = input()
    if text == "I":
        text = input()
        mismatch = find_mismatch(text)

        if mismatch == 0:
            print("Success")
        else:
            print(mismatch)



if __name__ == "__main__":
    main()
