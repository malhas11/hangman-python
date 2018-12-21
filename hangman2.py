from hangman_lib import *
import random

# This program WILL NOT RUN until you have added all the specified sub-programs
# Ensure that you test them first!

words = ["ant","baboon","badger","bat","bear","beaver","camel","cat","clam","cobra","cougar","coyote","crow","deer","dog","donkey","duck","eagle","ferret","fox","frog","goat","goose","hawk","lion","lizard","llama","mole","monkey","moose","mouse","mule","newt","otter","owl","panda","parrot","pigeon","python","rabbit","ram","rat","raven","rhino","salmon","seal","shark","sheep","skunk","sloth","snake","spider","stork","swan","tiger","toad","trout","turkey","turtle","weasel","whale","wolf","wombat","zebra"]

def main():
    game_over = False
    correct_letters = ""
    incorrect_letters = ""
    #guesses = ""
    
    
    
    hangman_index = 0

    secret_word = get_word()
    print("secret: ",secret_word) # For testing purposes only

    turns = len(secret_word)
    while not game_over:
        
                
        display_board(hangman_index,turns,incorrect_letters,correct_letters,secret_word)

        guess = get_guess(correct_letters , incorrect_letters)

        found_letter(guess ,secret_word)
        if found_letter(guess ,secret_word):
            correct_letters = correct_letters + guess
           
        else:
            incorrect_letters = incorrect_letters + guess
            hangman_index += 1
            
        
        
        
        game_over = has_won(secret_word, correct_letters,guess)
        if not game_over:
            game_over = has_lost(hangman_index,incorrect_letters,secret_word)

            if game_over:
                #print(HANGMAN[hangman_index])
                break
            
        if game_over:
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~ ################ ~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("Well DOne!")
            print("YOU WON, You guessed the secret word",secret_word)
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~ ################ ~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
        
#print (secret_word, correct_letters, incorrect_letters)

def found_letter(guess ,secret_word):
    if guess in secret_word:
        return True
    
        
def get_word():
    return (random.choice(words)) # secret word is stored in varaoble word

def get_guess(correct_letters , incorrect_letters):
    
    
    valid = True
    while valid:
        guess = input("\nEnter a guess ").lower() 
        if not guess.isalpha():
            print("That is not a letter. Please try again.")
            continue
        
        if len(guess) > 1:
            print("That is more than one letter. Please try again.")
            continue
        
        if guess in incorrect_letters or guess in correct_letters:
            print("You have already guessed that letter. Please try again.")
            continue
        else:
            
            break
    return guess

def display_board(hangman_index,turns,incorrect_letters,correct_letters,secret_word):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~[ H_A_N_G_M_A_N ]~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(HANGMAN[hangman_index])
    #print("You hav",turns,"turns to play")
    print()
    print("Incorrect Letters: ",incorrect_letters)
    print("Correct Letters: ",correct_letters)

    for letter in secret_word:
        if letter in correct_letters:
            print(letter, end=" ")
                #found_letter = True
        else:
            print('_', end=" ")

    print()
    
   
def has_won(secret_word, correct_letters,guess):
    
    ans = 0
    count = 0
    index = -1
    while count < len(secret_word):
        if secret_word[index] in correct_letters:
            ans = ans + 1        #ans counts the number of secretword in correct leters 
        count = count + 1
        index = index + 1
    if ans == len(secret_word):   #ans checks if the everyletter in secret word is in correct letter
        return True
    
   


def has_lost(hangman_index,incorrect_letters,secret_word):
    if len(incorrect_letters) >=6:
            print((HANGMAN[hangman_index]))
            print()
            print("You Lost")
            print("You Run out of Guesses")
            print("The secret word was: ",secret_word)
           
            return True
            
       
  

main()
