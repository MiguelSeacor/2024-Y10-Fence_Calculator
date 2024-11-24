# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    while True:
        error = "Please enter a number above zero"

        try:
            #ask the user for a number
            response = float(input(question))

            #check if the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine Goes here

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("What is the Width?: ")
    height = num_check("What is the Height?: ")
    cost = num_check("What is the Cost of fencing per meter?: ")

    # Calculate Area / Perimeter
    perimeter = 2 * (width + height)
    price = (perimeter * cost)

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Price: ${price:.2f}")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit: ")
    print()

print("Thank you for using the area / perimeter calculator :)")