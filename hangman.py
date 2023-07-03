#!/usr/bin/env python3

#import random
#words = ["saucepan", "spoon", "potato", "mouse"]
#solution = random.choice(words)

solution = "hello"
turns = 10
display = ""
letters_found = ""

for l in solution:
    display = display + "_ "

print(">> Welcome to the hangman <<\n")

while turns > 0:
    print("Guessing word : ", display)
    proposal = input("propose a letter : ")[0:1].lower()

    if proposal in solution:
        letters_found = letters_found + proposal
        print("-> Good point!")
    else:
        turns = turns - 1
        print("-> No\n")
        print("You still have ", turns, " attempt(s)\n")

    display = ""
    for letter in solution:
        if letter in letters_found:
            display += letter + " "
        else:
            display += "_ "

    if "_" not in display:
        print(">>> Won! <<<\n")
        break

print("* End of the game *")