# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
print()
animal = "Lion" # syntaxError: missing parentheses ""
animal_type = "cub"
number_of_teeth = 16

full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth.") # synatxError misisng parentheses (), missing format mode "f", logic error: wrong order of formating variables

print(full_spec) # missing parentheses (), removed extra space after print
print()
