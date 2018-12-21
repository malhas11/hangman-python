from hangman_lib import HANGMAN
words = ["ant","baboon","badger","bat","bear","beaver","camel","cat","clam","cobra","cougar","coyote","crow","deer","dog","donkey","duck","eagle","ferret","fox","frog","goat","goose","hawk","lion","lizard","llama","mole","monkey","moose","mouse","mule","newt","otter","owl","panda","parrot","pigeon","python","rabbit","ram","rat","raven","rhino","salmon","seal","shark","sheep","skunk","sloth","snake","spider","stork","swan","tiger","toad","trout","turkey","turtle","weasel","whale","wolf","wombat","zebra"]

def main():
    game_over = False
    correct_letters = str("")
    incorrect_letters = str("")
    alreadyguessed = ""
    index = 0
    
    secret_word = get_word() 

   
    while not game_over:
        display_board(secret_word, correct_letters, incorrect_letters, index)

        guess = get_guess(alreadyguessed)
        alreadyguessed = correct_letters + incorrect_letters
      

        if found_letter(guess, secret_word, index):
            correct_letters = correct_letters + guess
        else:
           incorrect_letters = incorrect_letters + guess
           index += 1

        game_over = has_won(secret_word, correct_letters)
        if not game_over:
            game_over = has_lost(incorrect_letters, secret_word, index)

    
            
    
def get_word():
    import random
    secret_word = random.choice(words)
    return secret_word

def display_board(secret_word, correct_letters, incorrect_letters, index):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~[ H_A_N_G_M_A_N ]~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(HANGMAN[index])
    print()
    print("incorrect letters: ", incorrect_letters)
    print("correct_letters: ", correct_letters)
    print()

    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
      
        

def get_guess(alreadyguessed):
    while True:
        print("guess a letter")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("please enter one letter")
        elif guess in alreadyguessed:
            print("you have already guessed this letter")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("please enter a LETTER")
        else:
            return guess
   
    
def found_letter(guess, secret_word, index):
    if guess in secret_word:
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~ ################ ~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        print("Well DOne!")
        print("YOU WON, You guessed the secret word",secret_word)
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~ ################ ~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        return True
        
            
        
         
def has_won(secret_word, correct_letters):
    if secret_word in correct_letters:
        return True
        
        
    else:
        game_over = False
        return False
        
    
    
def has_lost(incorrect_letters, secret_word, index):
     if len(incorrect_letters) >= 6:
            print()
            print(HANGMAN[index])
            print("You Lost")
            print("Game over")
            print("secret word: ", secret_word)
            return True

main()


        
        
    
   
        


    
        
        

        




