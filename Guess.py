import random
print("*** Welcome to Number Guessing Game *** ")
startrange=int(input("Enter the Starting Range of Number:"))
endrange=int(input("Enter the Ending Range of Number:"))
Random=random.randint(startrange,endrange)
chance=10
print("You Have",chance,"Choices")

for i in range(0,chance,1):
    uservalue=int(input("Enter the Number:"))
    if(uservalue==Random):
        print("Congratulations you have Won the Game in",chance,"try")
        break

    else:
        print("Wrong Guess!! Try Again.")
        chance=chance-1
        print("You have still",chance,"chances left")
    
    if(uservalue>Random):
        print("You Guess is Too High")
        print("----------------------------------------------------------------")


    else:
       print("You Guess is Too Low")
       print("----------------------------------------------------------------")
    
    if(chance==0):
        print("You Have",chance,"chance Better luck next time!!")








    
   
