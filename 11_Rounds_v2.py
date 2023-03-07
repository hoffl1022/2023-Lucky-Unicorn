import random

# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # adjust balance
    # if the random # is between 1 and 5
    # user gets a unicorn, add $4 to balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # if random # is between 6 and 36
    # user gets a donkey, subtract $1 from balance
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    # the token is either a horse or zebra
    # in either case subtract $0.50 from balance
    else:
        chosen = ("zebra", "horse")
        balance -= 0.5
        # randomly choose horse or zebra
        chosen = random.choice(chosen)

    # print what token the user received and their balance after they received that token
    print()
    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))
    print()

    if balance < 1:
        play_again = "xxx"
        print("Damn, you broke")

    else:
        play_again = input("press Enter to play again or type 'xxx' to quit")
        print()

print()
print("Final balance:", balance)

