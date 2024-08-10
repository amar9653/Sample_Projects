import random


'''1 for rock
-1 for paper 
0 for scissor'''



computer = random.choice([-1 , 1 , 0] )
youstr = input("Enter you choice in R , P , S: ").lower()

youdict = {"r": 1 , "p" : -1 , "s": 0} 
reversdict = {1 : "rock" , -1 : "paper" , 0 : "scissor"}

you = youdict[youstr]

print(f"You choose: {reversdict[you]} \nComputer Choose: {reversdict[computer]}")

if (computer == 1  and you == -1):
    print("You Win , Congrats")
elif (computer == 1  and you == 0):
    print("You Lose! , Better Luck next time")
elif (computer == 1  and you == 1):
    print("Draw , Try Again")
elif (computer == -1  and you == 0):
    print("You Win , Congrats")
elif (computer == -1  and you == 1):
    print("You Lose! , Better Luck next time")
elif (computer == -1  and you == -1):
    print("Draw , Try Again")
elif (computer == 0  and you == -1):
    print("You Lose! , Better Luck next time")
elif (computer == 0  and you == 1):
    print("You Win , Congrats")
elif (computer == 0  and you == 0):
    print("Draw , Try Again")
else:
    print("Your type input is wrong")




 


