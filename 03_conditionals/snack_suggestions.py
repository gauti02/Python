snack = input("What snack do you want to eat? ").lower() #converting user input to lowercase for easier comparison

print("You have chosen to eat " + snack)
print(f"user said: {snack}") #using f-string for string interpolation

if snack == "cookies" or snack == "samosa":
    print(f"Great choice! we will serve you {snack}")
else:
    print(f"Sorry, we don't have {snack} in our menu. Please choose something else.")