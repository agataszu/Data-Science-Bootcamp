# # This part of the program reads a string and makes each alternate character into an upper case, followed by a lower case character.

while True:
    greeting = input("\nHello! I can change an individual character of each word to upper and lower case, try me!: \n\n") #asking user for an input

# checkng for errors, program will keep asking user for a valid input, as numbers can't be converted to upper or lower case
    if greeting.isnumeric():
        print("WRONG! To see how I work, enter at least a few words made up of letters, not numbers!") 
    else:
        alternative_greeting = "" # placeholder for an altered string

        for i in range(len(greeting)):
            if i % 2 != 0:
                alternative_greeting += greeting[i].upper() # changing every other letter to an upper case
            else:
                alternative_greeting += greeting[i].lower() # or else leaving it lower case

        print (f"Here it is:\t {alternative_greeting} \n")
    
        break  # if the valid input(not number) is provided, exiting the loop


# This part of the porgram makes each alternative word lower and upper case.  
greeting = "Happy New Year to you and your family!"
print(f"\nNow, see what else I can do. This is an original sentence:\n\n\t\t{greeting}\n")

split_str = greeting.split(" ")
alternative_greeting = "" # placeholder for an altered greeting

for i in range(len(split_str)):
    if i % 2 != 0: 
        alternative_greeting += split_str[i].upper() + " " # changing every other word to an upper case
    else:
        alternative_greeting += split_str[i].lower() + " " # or else leaving it lower case

print(f"I can also change entire words by alternating between upper/lower case:\n\n\t\t{alternative_greeting}\n")
print("Thank you, goodbye!")
