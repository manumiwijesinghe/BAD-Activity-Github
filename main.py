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