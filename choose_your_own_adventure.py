name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. which way would you like to go? ")

if answer == "left":
   answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk arround and swim to swim accross: " ) 
   
   if answer == "swim":
       print("you swam acrross and were eaton by an alligator.")
   elif answer == "walk":
       print("You walked for many miles, ran out of water and you lost the game")
   else:
       print("not a valid option. You lose")
   
elif answer == "right":
   answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back ?") 
   
   if answer == "back":
       print("Yoyu go back and lose.")
   elif answer == "cross":
       answer = input("You cross the bridge and meet a stranger. Do you talk to them ?")
       
       if answer == "yes":
          print("You talk to the starnger and they give you gold. You WIN!") 
       elif answer == "no":
           print("You ignore the stranger and they are offended and you lose")
       
       else:
          print("not a valid option. You lose")
   else:
        print('Not a valid option. You lose.')
   
else:
    print('Not a valid option. You lose.')
