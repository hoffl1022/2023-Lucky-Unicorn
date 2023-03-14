# functions go here
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

# main routine goes here


how_much = num_check("how much would you like to play with? ", 0, 10)

print("you will be playing with ${}".format(how_much))
