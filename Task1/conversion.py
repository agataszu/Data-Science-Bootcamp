# Creating variables to store values

num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"


# Converting the variables, by assigning a new  type
num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1)

# Printing the variables
print(num1)
print(num2)
print(num3)
print(string1)


# Checking if string1 was indeed converted to an integer, by running a simple math question. I will add string1 to num1, it should give me 199.
print("\nThis is an integer: ")
print(string1 + num1)

# Checking that num3 was converted into a string. It should come with 150150150
print("\nThis is a string: ")
print(num3*3)