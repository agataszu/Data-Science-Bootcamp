# Below program will present a series of of Logical Errors"
print()


# wrong math is used, substraction instead of addition
apple_harvest1 = 17
apple_crop_harvest2 = 36

total_harvest=(f"The total apple harvest this year is {apple_harvest1 - apple_crop_harvest2}")
print(total_harvest)
print()

# printing numbers 1-10, incorrect loop condition, 10 is not included
for i in range(1, 10):
    print(i)
print()

# wrong comparison used for the if statement, it should be reversed to ">"
age = int(input("Enter your age: "))
if age < 18:
    print("You are allowed to legally drink alcohol.")
else:
    print("Sorry, you are under the legal age to consume alcohol, you cannot buy this drink.")
print()


# wrong condition for checking if it's sunny, it should be if is_sunny !=, or if is_sunny == "yes"
is_sunny = input("Is it sunny? (yes/no): ")

if is_sunny == "no":
    print("Remember to apply sunscreen.")
else:
    print("No need for skin protection.")