# Explain the tool to a user to gain a right input, a number instead of letters
print("This prgoramme will help you calcuate the area of a triangle. You will be asked to enter all three lengths to perform the calculaiton.")
print("Please note: the sum of two side lengths has to exceed the length of the third side.")
print()

# Request the input
a = float(input("Enter length of the first side: "))
b = float(input("Enter length of the second side: "))
c = float(input("Enter length of the third side: "))

import math
# calculating a semi-perimeter
s = (a + b + c)/2

# calculating the area
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print()
print("The area of the triangle is:", area)