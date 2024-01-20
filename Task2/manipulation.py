# asking user for an input
str_manip = input("Please write a simple sentence: ") 
print("For refrence, this is your sentence: " + str_manip)
print()

#counting the length of an input
str_len = len(str_manip)
print(str_len)
print()

# identifying the last letter of the sentence and replacing the occurence with @
last_letter = str_manip[-1] 
str_modified = str_manip.replace(last_letter, "@")
print(str_modified)
print()

# printing the last 3 characters of the sentence backwards
last_letters_reverse = str_manip[-3:]
print("The last three letters in reverse: " + last_letters_reverse[::-1])
print()

# create a five-letter word that is made up of the first three characetrs and the last two characters in str_manip
first_three_chars = str_manip[0:3]
last_two_chars = str_manip [-2:]
new_word = str(first_three_chars + last_two_chars)
print("This is a word created from the first three and the last two letters of this sentence: " + new_word)
print()