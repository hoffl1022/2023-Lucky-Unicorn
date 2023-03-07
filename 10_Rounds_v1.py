# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print("*** Round #{} ***".format(rounds_played))
    balance -= 1
    print("balance: ", balance)
    print()

    if balance < 1:
        play_again = "xxx"
        print("you broke")
    else:
        play_again = input("press Enter to play again or type 'xxx' to quit")

print()
print("Final balance:", balance)

