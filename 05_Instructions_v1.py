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

print("program continues")