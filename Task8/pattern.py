# Task: Write code to output the star pattern shown below, using an if-else  statement in combination with a single for loop
#
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


# there is 9 lines in the pattern above, it has to be therefore lopped 9 times
# increase the number of stars in pattern until the 5th line is reached
# then from 6th row including, decreas the pattern

print("\nThis is the required pattern: \n")

star_pattern = "*"

for line in range (1,10):

    if line <= 5:
        print(star_pattern * line) # increasing pattern

    else:
        print(star_pattern * (10 - line)) # decreasing pattern

print()