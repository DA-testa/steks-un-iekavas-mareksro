# python3
# Mareks Rozenblats 221RDB313 2.grupa

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
        return opening_brackets_stack[-1].position
    return "Success"


def main():
    text = input()
    text = ("Ievadiet F vai I:\n")
    #izvele = input()
    #if izvele == "F":
        #fails = input("Ievadiet faila nosaukumu:\n")
        #with open(fails, "r") as f:
            #text = f.read().strip()
    #elif izvele == "I":
       # text = input("Ievadiet iekavas:\n ")
    mismatch = find_mismatch(text)
    print(mismatch)
    #else:
       #print("Invalid choice\n")
        #return
    

if __name__ == "__main__":
    main()