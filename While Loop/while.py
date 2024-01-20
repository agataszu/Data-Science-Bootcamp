# program will continually ask the user to enter a number

total = 0
count = 0



while True:
    try:
        # the program should stop when entering -1
        user_input = float(input("Please enter a number (or else type '-1' to exit the program): ")) 

        if user_input == -1:
            break

        total += user_input
        count += 1

    except ValueError:
        print("Please enter a valid number.")

    # the program must then calculate the average of the numbers entered, excluding -1

average = total / count
print(f"\nThe average value of the numbers entered is:\t{average}\n")

