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

def num_check(question, low, high):
    error = "please enter a whole number between 1 and 10\n"

    while True:
        try:
            # ask the response
            response = int(input(question))

            # if the the response is too low / too high give
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
    print("The rules of the game go here")
    print()
    return ""

# Main routine goes here
played_before = yes_no("have you played this game before? ")

if played_before == "no":
    instructions()

# ask user how much they want to play with
how_much = num_check("How much would you like to play with? ", 0, 10)

print()
print("You will be playing with ${}".format(how_much))
