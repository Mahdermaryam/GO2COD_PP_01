#this simple code do is 
#made by mahderemayiaram


#importing a random module
import random

#creating a function that 
def guessing_game():

    #getting a secret number using a randint function from random module and give to the variable secret_number
    secret_number=random.randint(1,100)
    count=0 #setting a counter that count how many time they try

    print("WELCOME TO THIS GUESIING GAME")
    gussed_number=int(input(f"I HAVE A NUMBER IN MY MING ,AND IT IS BETWEEN 1 AND 100 ,GUESS WHAT IT IS  : "))

    while secret_number != gussed_number:
        
        
        if secret_number > gussed_number:
            print("TOO LOW , ENTER AGAIN: ", end=" ")
        else:
            print("TOO HIRH , ENTER AGAIN: ", end=" ")

        gussed_number=int(input())
        count+=1

    print("❁´◡`❁ CONGRATULATION ❁´◡`❁,YOU GOT IT ")
    print("It takes you " , count ," times to get it")
    
            
    
guessing_game()
