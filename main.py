# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            pass
            opening_brackets_stack.append(Bracket(next,i+1))
            

        if next in ")]}":
            # Process closing bracket, write your code here
            pass
            if len(opening_brackets_stack) == 0 or not are_matching (opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
            
    if opening_brackets_stack:
        return opening_brackets_stack[0].position +1
    else :
        return "Success"



def main():
    text = input()
    izvele = input("Ievadiet F vai I: ")
    if izvele == "F":
        fails = input("Ievadiet faila nosaukumu: ")
        with open(fails, "r") as f:
            text = f.read().strip()
    elif izvele == "I":
        text = input("Ievadiet iekavas: ")
    else:
        print("Invalid choice")
        return
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
