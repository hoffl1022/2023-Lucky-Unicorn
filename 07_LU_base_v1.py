import random

# Functions go here


# checks whether the user answers yes or no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")


# asks the user for a number
def num_check(question, low, high):
    error = "please enter a whole number between 1 and 10\n"

    while True:
        try:
            # ask the response
            response = int(input(question))

            # if the response is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# displays the instructions, returns ""
def instructions():
    print("**** How to Play****")
    print()
    print("First you need to enter how much money")
    print("you would like to play with ($1 - $10 in full dollars)")
    print("Then you can press enter to play")
    print()
    print("A random animal will be generated, depending on which animal you get")
    print("you can either gain or lose money")
    print()
    print("if you get a Unicorn you will win $4")
    print("if you get a horse / zebra you will lose $0.50")
    print("if you get a donkey you will lose $1")
    print()
    print("if you end up with less that $1 the game will automatically end")
    print("or you can type 'xxx' at any time to manually end the game")
    print()
    return ""


# generate a decorated statement, returns ""
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine goes here

welcome = "Welcome to lucky unicorn!"
statement_generator(welcome, "#")
print()

played_before = yes_no("===have you played this game before?=== ")
print()

if played_before == "no":
    instructions()

# ask user how much they want to play with
how_much = num_check("===How much would you like to play with?=== ", 0, 10)
print()

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again != "xxx":

    # increase # of rounds played
    rounds_played += 1

    # print round number

    round_num = ("Round #{}".format(rounds_played))

    statement_generator(round_num, "*")
    print()

    chosen_num = random.randint(1, 100)

    # adjust balance
    # if the random # is between 1 and 5
    # user gets a unicorn, add $4 to balance
    if 1 <= chosen_num <= 5:
        chosen = "Unicorn"
        balance += 4
        prize_decoration = "!"

    # if random # is between 6 and 36
    # user gets a donkey, subtract $1 from balance
    elif 6 <= chosen_num <= 36:
        chosen = "Donkey"
        balance -= 1
        prize_decoration = "D"

    # the token is either a horse or zebra
    # in either case subtract $0.50 from balance
    else:
        # if the number is even set chosen to horse
        if chosen_num % 2 == 0:
            chosen = "Horse"
            prize_decoration = "H"

        else:
            chosen = "Zebra"
            prize_decoration = "Z"
        balance -= 0.5

    # print what token the user received and their balance after they received that token

    outcome = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"

    else:
        play_again = input("Press Enter to play again or type 'xxx' to quit")
        print()

print()
statement_generator("Results", "=")

print()
print(f"Final balance: ${balance:.2f}")
print("Thank you for playing")
