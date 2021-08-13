import random
randNumber = random.randint(1,100)
# print(randNumber)
userGuess = None
guesses = 0

print(" \t \t \t \t Guess the Number Game\n \n")

if(randNumber<=20):
    print("The random no. is in 20")
elif(randNumber<=40):
    print("The random no. is in between 20 and 40")
elif(randNumber<=60):
    print("The random no. is in between 40 and 60")
elif(randNumber<=80):
    print("The random no. is in between 60 and 80")
elif(randNumber<=100):
    print("The random no. is in between 80 and 100")
while(userGuess != randNumber):
    userGuess = int(input("Enter the guessing number:\n"))
    guesses +=1
    if (userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guesed it wrong! Enter a smaller number")
        else:
            print("You guesed it wrong! Enter a larger number")
    

print(f"You guessed the number in {guesses} guesses")
with open("Hiscore_guess_game.txt","r") as f:
    hiscore = int(f.read())
if(guesses<hiscore):
    print("You have just broken the highscore!")
    with open("Hiscore_guess_game.txt","w") as f:
        f.write(str(guesses))