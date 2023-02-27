
show_instructions = ""
while show_instructions.lower() != "end":
    # ask user if they have played before
    show_instructions = input("have you played before? ") .lower()

    # if they say yes output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

    # if they say no output 'display instructions
    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("display instructions")

# if the answer is invalid print an error
    else:
        print("please answer yes / no")