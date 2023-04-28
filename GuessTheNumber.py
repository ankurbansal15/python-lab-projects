import random
while(True):
    print("Enter the Range of Numbers")
    min = int(input("Enter the Minima of Range:"))
    max = int(input("Enter the Maxima of Range:"))
    if(min > max):
      print("Your Minima is greater than the Maxima, Try Agrain")
      continue
    else:
       while(True):
        user_choice = int(input("Enter Your Choice:"))
        sys_choice = random.randint(min,max)
        if(user_choice == sys_choice):
            print("Congur1alations, You Guess it correct")
            break
        else:
            print("Sorry, Your Guss is wrong, Try Agrain ")
       


