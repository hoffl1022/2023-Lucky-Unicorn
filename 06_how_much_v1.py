# functions go here


# main routine goes here

error = "please enter a whole number between 1 and 10\n"

while True:
    try:
        # ask the response
        response = int(input("how much would you like to play with? "))

        # if the the response is too low / too high give
        if  0 < response <= 10 :
            print("you have chosen to play with ${}".format(response))

        # output an error
        else:
            print(error)

    except ValueError:
        print(error)