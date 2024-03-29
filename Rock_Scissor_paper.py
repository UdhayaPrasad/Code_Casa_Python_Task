import random
print("Rock Paper Scissor")

while True:
    print(" 1. Rock \n 2. Paper \n 3. Scissor \n 4. Exit ")
    choice = int(input("Enter your choice:"))

    if(choice==1):
        choice='Rock'

    elif(choice==2):
        choice='Paper'

    elif(choice==3):
        choice='Scissor'

    elif(choice==4):
        print("Exiting from the game")
        break

    print("Your Choice : " + choice)

    computer_generated = random.randint(1,3)

    if(computer_generated==1):
        computer_generated='Rock'

    elif (computer_generated==2):
        computer_generated='Paper'

    elif(computer_generated==3):
        computer_generated='Scissor'

    print("Random choice: " + computer_generated)

    if(choice==computer_generated):
        print("Match Draw")
        print('--------------------------------')

    elif(choice=="Rock" and computer_generated=="Scissor"): 
        print("Rock wins..")
        print("You Win!!!")
        print('--------------------------------')

    elif(choice=="Rock" and computer_generated=="Paper"): 
        print("Paper wins")
        print("Computer Wins!!!")
        print('--------------------------------')

    elif(choice=="Paper" and computer_generated=="Rock"):
        print("Paper wins..")
        print("You win!")
        print('--------------------------------')

    elif(choice=="Scissor" and computer_generated=="Paper"): 
        print("Scissors wins..")
        print("You win!")
        print('--------------------------------')

    elif(choice=="Paper" and computer_generated=="Scissor"): 
        print("Scissors wins..")
        print('Computer wins!!')
        print('--------------------------------')

    elif(choice=="Scissor" and computer_generated=="Rock"):
        print("Rock wins..")
        print('Computer wins!!')
        print('--------------------------------')
