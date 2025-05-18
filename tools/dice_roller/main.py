#imports
from roller import roll_dice

#main_loop

#gui setup 



#testing
sides = int(input("What kind of dice are w rolling? "))
count = int(input("How many dice are we rolling? "))
modifier = int(input("What are your modifiers? (enter number , sero if none) "))


answer = roll_dice(sides,count)

print(answer)

want_total = input("would you like the total? (y/n)")
total_roll = 0
if want_total.lower() == "y":
    total_roll = sum(answer)
    total_roll = total_roll + modifier
    print("The total is:", total_roll)
else:
    pass
