# Design a program that determines the award a person competing in a triathlon will receie
# your program should read in the times (in minutes) for all three events of a triathlon, namely swimming, cycling and running


# QUALIFYING CRITERIA
# 0-100 minutes - Provincial Colours
# 101-105 minute - Provincial Half Colours
# 106-110 minute - Provincial Scroll
# 111 + - No Award 

swimming = int(input("Enter your swimming time in minutes: "))
cycling = int(input("Enter your cycling time in minutes: "))
running = int(input("Enter yourrunning time in minutes: "))
print()

# calculate and display the total time taken to complete the thriatlon
thriatlon_total = swimming + cycling + running
print(f"The total time it took you to complete this thriatlon is {thriatlon_total} minutes")
print()

# award is based on the total time taken to complete triathlon
if thriatlon_total <= 100:
    print("You have been awarded: Provincial Colours\n")

elif thriatlon_total <= 105 and thriatlon_total >= 100:
    print("You have been awarded: Provincial Half Colours")

elif thriatlon_total  >= 106 and thriatlon_total <= 110:
    print("You have been awarded: Provincial Scroll")

else:
    print("Sorry, you were too slow: No Award ")

