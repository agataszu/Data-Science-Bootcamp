# Requesting user's input to enter a name(string) of a favourite restaurant
string_fav = input("Please enter a name of your favourite restaurant: ")
string_fav = str(string_fav)

# Requesting user's input to enter a favourite number(integer)
int_fav = input("Please enter your favourite number: ")
int_fav = int(int_fav)

print(string_fav)
print(int_fav)


string_fav = int(string_fav)
# when casting a string into an integer a valueError comes up. This is because a string contains letters which are not a numeric values
