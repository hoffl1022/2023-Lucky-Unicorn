import random

# main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE

# testing loop to generate 100 tokens
for item in range(0, 20):
    chosen_num = random.randint(1, 100)

    # adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        chosen = ("zebra", "horse")
        balance -= 0.5
        chosen = random.choice(chosen)

    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

print()
print("starting balance: ${:.2f}".format(STARTING_BALANCE))
print("final balance: ${:.2f}".format(balance))
