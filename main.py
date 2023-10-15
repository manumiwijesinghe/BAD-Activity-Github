import time
import random
from WordList import WDictionary

name = input("Tell me your name? ")#Get the user's name
name = name.upper()

print("Hello, " + name, "Welcome to the WORD BENDER!")
time.sleep(1)

def Word_Bender():
    word =random.choice(WDictionary)
    words=words.lower()
    RLetter=random.choice(words)#selecting random letter to show
    print("*****************************************")
    print(""+name,"be ready to play the game!!!")
    print("Start guessing... Go..! ")
    print("You have 10 tries")
    time.sleep(0.5)
    guessedletters = RLetter + " _" * (len(words) - 1)
    tries = 10

# Create a while loop to repeat the code
    while tries > 0:
        F = 0 #count how many times user will fail
        for letter in words:
            #print the correct guesses
            if letter in guessedletters:
                print(letter, end=" ")

            else:
                print("_", end=" ")
                F += 1
        print()
        if  F == 0: #When there isn't any failuer user will win
            print("Congratulations.!!! " + name, "You won!")
            print()
            time.sleep(1.0)
            break
        print ()