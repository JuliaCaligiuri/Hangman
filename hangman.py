#Program to implement the game hangman with different themes
import random

def menu():
    print("Welcome to hangman! Enter \"#\" anytime to quit")
    print("Please choose your theme: ")
    #Printing all of the themes by using the keys of the dictionary
    for key in wordDict:
        print(key)
    theme = input()
    if theme == "#":
        print("Have a nice day!")
        quit()
    word = random.choice(wordDict[theme])
    return word
    

def printBoard(word, lettersGuessed):
    #prints the word and the hangman
    print("The word to guess is: ")
    output = ""
    for x in word:
        if x.lower() in lettersGuessed or x.upper() in lettersGuessed:
            output+= x
        elif x == " ":
            output+= " "
        else:
            output+= "_"
    print(output)
    
def buildHangman(lettersMissed):
    if len(lettersMissed) == 0:
        print(" -----------")
        print(" |         |")
        print(" |\n"*8)
    elif len(lettersMissed) == 1:
        print(" -----------")
        print(" |         |")
        print(" |        ---")
        print(" |       |   |")
        print(" |        ---")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
    elif len(lettersMissed) == 2:
        print(" -----------")
        print(" |         |")
        print(" |        ---")
        print(" |       |   |")
        print(" |        ---")
        print(" |         |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
    elif len(lettersMissed) == 3:
        print(" -----------")
        print(" |         |")
        print(" |        ---")
        print(" |       |   |")
        print(" |        ---")
        print(" |         |")
        print(" |         |")
        print(" |")
        print(" |")
        print(" |")
    elif len(lettersMissed) == 4:
        print(" -----------")
        print(" |         |")
        print(" |        ---")
        print(" |       |   |")
        print(" |        ---")
        print(" |         |")
        print(" |         |")
        print(" |         |")
        print(" |")
        print(" |")
    elif len(lettersMissed) == 5:
        print(" -----------")
        print(" |         |")
        print(" |        ---")
        print(" |       |   |")
        print(" |        ---")
        print(" |         |")
        print(" |         |")
        print(" |         |")
        print(" |        /")
        print(" |       /")
    elif len(lettersMissed) == 6:
        print(" -----------")
        print(" |         |")
        print(" |        ---")
        print(" |       |   |")
        print(" |        ---")
        print(" |         |")
        print(" |         |")
        print(" |         |")
        print(" |        / \\")
        print(" |       /   \\")
    elif len(lettersMissed) == 7:
        print(" -----------")
        print(" |         |")
        print(" |        ---")
        print(" |       |   |")
        print(" |        ---")
        print(" |       \ |")
        print(" |        \|")
        print(" |         |")
        print(" |        / \\")
        print(" |       /   \\")
    elif len(lettersMissed) == 8:
        print(" -----------")
        print(" |         |")
        print(" |        ---")
        print(" |       |   |")
        print(" |        ---")
        print(" |       \ | /")
        print(" |        \|/")
        print(" |         |")
        print(" |        / \\")
        print(" |       /   \\")
        

def pickLetter(word, lettersGuessed, lettersMissed):
    buildHangman(lettersMissed)
    printBoard(word, lettersGuessed)
    print("Please enter a letter")
    letter = input()
    if letter == "#":
        print("Have a nice day!")
        quit()
    if letter.upper() in lettersGuessed or letter.upper() in lettersMissed or letter.lower() in lettersGuessed or letter.lower() in lettersMissed:
        print("You have already tried this letter, please try again")
        letter = input()
    #Checking if the letter is in the chosen word or not
    if letter.upper() in word:
        lettersGuessed.append(letter)
        print("This letter is in the word.")
    elif letter.lower() in word:
        lettersGuessed.append(letter)
        print("This letter is in the word.")
    else:
        lettersMissed.append(letter)
        print("This letter is not in the word. A part to the hangman was added.")
    #Repeating the function if the guessing isn't done, or breaking if won or lost game
    checkFinished(word, lettersGuessed, lettersMissed)


def checkFinished(word, lettersGuessed, lettersMissed):
    #Checking if user won game
    correct = 0
    for x in word:
        if x.lower() in lettersGuessed or x.upper() in lettersGuessed:
            correct += 1
    if correct == (len(word)-word.count(' ')):
        print("Congratulations, you have successfully guessed the word "+word+" and won the game! Thanks for playing.")
        return
    #Checking if user lost game
    if len(lettersMissed) >= 8:
        print("Unfortunately, you have lost hangman. The word was "+word+". Thanks for playing.")
        return
    #If the game is still going, prompting user to pick another letter
    pickLetter(word, lettersGuessed, lettersMissed)

#Start of main function
#Creating a dictionary of different themes and lists of word options
wordDict = {"Animals": ["Fox", "Bear", "Dolphin", "Shark", "Whale", "Fish", "Cat", "Bird", "Seal", "Turtle", "Tortise", "Frog", "Horse", "Goat", "Jaguar", "Lion", "Cheetah", "Leopard", "Beetle", "Spider", "Snake", "Crocodile", "Elephant", "Kangaroo", "Gorilla", "Butterfly", "Scorpion"], "Artists": ["Taylor Swift", "Drake", "Kanye West", "Lorde", "Khalid", "Coldplay", "Journey", "Beyonce", "Ariana Grande", "Noah Kahan", "Post Malone", "Fleetwood Mac", "Rihanna", "Frank Ocean", "The Weeknd", "Calvin Harris", "John Summit", "Adele", "Morgan Wallen", "REO Speedwagon"], "Classic Movies": ["The Godfather", "The Breakfast Club", "The Shining", "The Outsiders", "To Kill a Mockingbird", "Dead Poets Society", "Dirty Dancing", "The Notebook", "Casablanca", "Goodfellas", "Grease", "Jaws", "Star Wars", "Pulp Fiction", "Titanic", "Ghostbusters", "Lord of the Rings"]}

tryAgain = True
while tryAgain:
    lettersMissed = []
    lettersGuessed = []
    word = menu()
    pickLetter(word, lettersGuessed, lettersMissed)
    print("Would you like to try again? Please enter Y or N")
    responding = True

    while(responding):
        response = input()
        if(response=="N" or response=="n" or response=="#"):
            tryAgain = False
            responding = False
            print("Thanks for playing!")
        elif(response=="Y" or response=="y"):
            responding = False
        else:
            print("Sorry, we could'nt recognize this answer. Please try again by responding with Y or N.")

