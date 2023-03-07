import random

# main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE

# testing loop to generate 100 tokens
for item in range(0, 20):
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
    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

# print starting and final balance
print()
print("starting balance: ${:.2f}".format(STARTING_BALANCE))
print("final balance: ${:.2f}".format(balance))
