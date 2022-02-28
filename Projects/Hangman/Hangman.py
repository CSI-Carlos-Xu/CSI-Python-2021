
import random 

# Word list
word_list =  ["gimnasia", "tenis", "ciclismo", "rugby", "boliche", "vela", "baloncesto", "voleibol", "remo", "surfing", "patinaje", "balompie", "natacion", "pelota", "ajedrez", "golf", "badminton", "boxeo", "esgrima", "hockey"]
invalid_specialcaracters= ["!","@","~","`","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","|",":",";","'","<",",",".",">","/","?"]
invalid_numbers= ["9","8","7","6","5","4","3","2","1","0"]

# To choose a word from the list randomly
def print_word(word_list):
    word = random.choice(word_list)
    return word.lower()


def game(word):
    word_space = "-"* len(word)
    guess = False
    guess_letters = []
    # guess_word = []
    attempts = 5
    print("Welcome to Hangman")
    print(word_space)
    while not guess and attempts > 0:
        think = input("Choose a letter or word").lower()
        if len(think) == 1 and think.isalpha():
            if think in guess_letters:
                print ("Letter already used", think)
            elif think not in word:
                print("Incorrect" ,think)
                attempts -=1
                guess_letters.append(think)
            else:
                print("Correct", think, "is in the word")
                guess_letters.append(think)
                word_as_list = list(word_space)
                indices = [i for i, letter in enumerate(word) if letter == think]
                for index in indices:
                    word_as_list[index] = think
                word_space = "".join(word_as_list)
                if "-" not in word_space:
                    guess = True
        else:
            print("invalid input")
        print(dis_hangman(attempts))
        print(word_space)
    if guess:
        print("You Win")
    else:
        print("No more attempts!!!")
            

def dis_hangman(attempts):
    steps = [ """ 

--------
|
|
|
|
|
>>>>>>>>>>>>>>>>
""",
"""
--------
|     |
|
|
|
|
>>>>>>>>>>>>>>>>
""",
"""
--------
|     |
|     O
|
|
|
>>>>>>>>>>>>>>>>
""",
"""
--------
|     |
|     O
|     |
|
|
>>>>>>>>>>>>>>>>
""",
"""
--------
|     |
|     O
|    /|\\
|
|
>>>>>>>>>>>>>>>>
""",
"""
--------
|     |
|     O
|    /|\\
|    ? ?
|
>>>>>>>>>>>>>>>>
""",
    ]
    return steps[attempts]
def gameloop():
    word = print_word(word_list)
    game(word)
    while input("Play again? (Yes/No").lower() == "Yes":
        word = print_word(word_list)
        game(word)

if __name__ == "__game loop__":
    gameloop()



   





    # if(letter.isalpha()):
    #     print("the given character does not contain special characters")   


    # elif(letter.isalpha):
    #     print("Invalid")



