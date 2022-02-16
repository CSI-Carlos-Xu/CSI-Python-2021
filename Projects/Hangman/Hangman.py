from imp import is_frozen
import random 
word_list = ["gimnasia", "tenis", "ciclismo", "rugby", "boliche", "vela", "baloncesto", "voleibol", "remo", "surfing", "patinaje", "balompie", "natacion", "pelota", "ajedrez", "golf", "badminton", "boxeo", "esgrima", "hockey"]

steps = [""" 

--------
|
|
|
|
|
>>>>>>>>>>>>>>>>

--------
|     |
|
|
|
|
>>>>>>>>>>>>>>>>

--------
|     |
|     O
|
|
|
>>>>>>>>>>>>>>>>

--------
|     |
|     O
|     |
|
|
>>>>>>>>>>>>>>>>

--------
|     |
|     O
|    -|-
|
|
>>>>>>>>>>>>>>>>

--------
|     |
|     O
|    -|-
|    ? ?
|
>>>>>>>>>>>>>>>>


"""]
        

print(steps[0])

def get_word():
    word_list =  ["gimnasia", "tenis", "ciclismo", "rugby", "boliche", "vela", "baloncesto", "voleibol", "remo", "surfing", "patinaje", "balompie", "natacion", "pelota", "ajedrez", "golf", "badminton", "boxeo", "esgrima", "hockey"]
    return random.choice(word_list)

def find_input():

    letter = input("choose letter")

    # if(letter != #)

    while not guessed and tries > 0:
        guess = input("Guess the word:").upper()
        if len(guess) ==1 and guess.isalpha():
            if guess in guessed_letters:
                print("already used that letter", guess)
                elif guess not in word:
                    print(guess,"Not the word:")




    # if(letter.isalpha()):
    #     print("the given character does not contain special characters")   


    # elif(letter.isalpha):
    #     print("Invalid")



