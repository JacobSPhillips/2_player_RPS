print("...rock...\n...paper...\n...scissors...")

choice1 = input("Enter player 1's choice: ")

print()
print("*******NO CHEATING********\n" * 30)

choice2 = input("Enter player 2's choice: ")

choice1 = choice1.lower()
choice2 = choice2.lower()

print("SHOOT")

# checking to see if p1's answers are valid
if choice1 == "rock" or choice1 == "paper" or choice1 == "scissors":

    # checking to see if p2 answers are valid
    if choice2 == "rock" or choice2 == "paper" or choice2 == "scissors":

        # determining if p2 won
        if choice1 == "rock" and choice2 == "paper" or \
                (choice1 == "paper" and choice2 == "scissors") or \
                (choice1 == "scissors" and choice2 == "rock"):
            print("Player 2 wins!!")
        # checking if answers are equal
        elif choice1 == choice2:
            print("It's a tie")
        # if neither of the prior, p1 must have won
        else:
            print("Player 1 wins!!")

    else:
        print("Something went wrong.")

else:
    print("something went wrong.")
    