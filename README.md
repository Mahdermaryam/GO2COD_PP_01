# GO2COD_PP_01
what this code does is 
-The random.randint(1, 100) function generates a random integer between 1 and 100 and assigns it to the variable secret_number.
-A count variable is initialized to 0. This variable will keep track of how many attempts the user makes to guess the correct number.
-ask the user to enter his gussed number and give to the variable called gussed_number
-then there is a while loop ,which let the user to gussed many time until he find the number 
-so the condition of the loop will be as long as the gussed_number and the secret_number are not equal 
-in the loop :-
        .first it check wheather the gussed_number is less than the secret_number,if it is ture it gives the user a hint (too low)
        .if the gussed_number is greater than the secret_number it will say (too high)
        .then it asks the user to enter the user another gusse,since the users gusse is not correct
        .and increase the amount of the counter by one
-finally if the user find the number the while loop will not execute so it will print the CONGRATULATION statement
