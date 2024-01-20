# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print()
print("Welcome to the error program") #syntax error, () parentheses missing, extra space after print
print("\n")   # syntax error, unecessary indentation, () missing

# syntax error, anothe unnecessary indentation in the entire block below

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # syntax error: removing unnecesary "years old", and one extra "=", as it is a variable, not equal
age_Str = str(age_Str)
age = int(age_Str) 
print("I'm " + age_Str + "years old.") # syntax: adding extra space after "I'm", using the right version of input, by choosing age_Str

# Variables declaring additional years and printing the total years of age
years_from_now = "3"
years_from_now = int(years_from_now)
total_years = age + years_from_now # runtime error: unable to concatinate string with integer, changed "years_from_now" to an int

print(f"The total number of years: + {total_years}") #syntaxError, missing () parentheses, runtime: "answer years" not defined, missing function

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # SyntaxError - total is not defined, we need to use existing variable called exactly "total_years"

print(f"In 3 years and 6 months, I'll be {total_months + 6} months old") #syntaxError, missing () parentheses, missing format editing, logicError: we need to add 6 months that is missing

print()

#HINT, 330 months is the correct answer

