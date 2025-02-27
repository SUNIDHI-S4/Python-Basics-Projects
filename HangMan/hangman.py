import random
from words import words
import string
from hangman_visuals import lives_visual_dict

# print(words)

def get_valid_word(words) :
    word = random.choice(words)
    while ' ' in word or '-' in word or len(word)>10:
        word = random.choice(words)
    return word.upper()

def hangman() :
    word = get_valid_word(words) 
    word_letters = set(word)    #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    #letters user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0 :

        print(f"\n\n\nYou have {lives} lives left and you have used the letters : ",' '.join(used_letters))
        print(lives_visual_dict[lives])
        word_list = [letter if letter in used_letters else '_' for letter in word ]
        print("Word : ","".join(word_list))
        user_letter = input("Guess a letter : ").upper()
        if user_letter in alphabet - used_letters :
            used_letters.add(user_letter)
            if user_letter in word_letters :
                word_letters.remove(user_letter)
            else : 
                lives -= 1
                print('Letter is not in the word.')
        
        elif user_letter in used_letters :
            print("You have already used that letter. Try again.")

        else :
            print("Invalid character")
    
    #gets here when word_letter == '' or when lives == 0
    if lives == 0 :
        print(f"You died! The word was {word} .")
    else :
        print(f"You have guessed the word {word} correctly !!")

hangman()