import random
start = input ("Do you wanna play a game? (Y / N) ")
if start == "y":
    user = random.randint (1,6)
    print ("You rolled a" , user,"!")
    comp = random.randint (1,6)
    print ("The computer rolled a ", comp,"!")
    if user > comp:
        print ("You win!")
        input ("Press enter to exit ")
    elif user < comp:
        print ("You lose!")
        input ("Press enter to exit ")
    else:
        print ("It's a draw!")
        input ("Press enter to exit ")
else:
    print ("Erro, please input 'y' or 'n'. ")
    input ("Press enter, exit and run the program again.")
