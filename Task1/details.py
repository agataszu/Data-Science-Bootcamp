
# Request the following information from the user: "name", "age", "house number", "street name"

name = input("What is your name?: ")
age = input("How old are you?: ")
house_number = input("Please enter your house number: ")
street_name = input("Please enter your street name: ")

# Print the statement below using gathered information.
# "This is {name}, who is {age} years old and lives at {house number} {} on {street name}" 
print()
print(f"This is {name}, who is {age} years old and lives at house number {house_number} on {street_name}.")
