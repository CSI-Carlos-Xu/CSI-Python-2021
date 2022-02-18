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

invalid_specialcaracters= ["!","@","~","`","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","|",":",";","'","<",",",".",">","/","?"]
invalid_numbers= ["9","8","7","6","5","4","3","2","1","0"]

def print_word():
    word_list =  ["gimnasia", "tenis", "ciclismo", "rugby", "boliche", "vela", "baloncesto", "voleibol", "remo", "surfing", "patinaje", "balompie", "natacion", "pelota", "ajedrez", "golf", "badminton", "boxeo", "esgrima", "hockey"]
    return random.choice(word_list)

print_word()

def get_input():

    while(True):
        letter = input("Chose your letter")

        if(len(letter)!= 1):
            print("Only choose one letter")
            continue

        if(letter in invalid_specialcaracters):
            print("It can't be a special characters")
            continue

        if(letter in invalid_numbers):
            print("No numbers are allowed")
            continue

        return letter

    def print_word():
         temp:str = ""
         for letter in my_word
         if (letter not in )


    



   





    # if(letter.isalpha()):
    #     print("the given character does not contain special characters")   


    # elif(letter.isalpha):
    #     print("Invalid")



