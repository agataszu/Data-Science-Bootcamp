# The program will be used to output a variety of responses determined by the data the user enters
# Write code to take in  user's age and store it in an integer variable called age


# age > 100         # "Sorry, you are dead."
# age => 65 <100    # "Enjoy your retirement!"
# age => 40 <65     # "You're over the hill."
# age < 40 > 25     # "Age is but a number."
# age == 21         # "ongrats on your 21st!"
# age => 12 <21     # "Age is but a number.
# age < 12          # "You qualify for the kiddie discount."

while True:
    age = int(input("Please enter your age: "))

    if age < 12:
        print("You qualify for the kiddie discount.")
    elif age < 40:
        if age == 21:
            print("Congrats on your 21st!")
        else:
            print("Age is but a number")
    elif age >= 65:
        if age <= 100:
            print("Enjoy your retirement!")
        else:
            print("Sorry, you are dead")
    elif age < 65:
        print("You're over the hill.")

