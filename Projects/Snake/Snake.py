import pygame #It calls the module where the game is.
pygame.init() #This step initialize the game.
dis=pygame.display.set_mode((400,300)) #This creates a display for the game. 
pygame.display.update() #This step updates the display of the screen. 
pygame.display.set_caption('Snake game by Edureka') #This string names the screen. 
game_over=False #Here, a variable is created to define that the game_over equals false.
while not game_over: #This is a loop that will keep repeating itself until the gameover variable has been set to true. 
    for event in pygame.event.get(): #get every event as a list and run a forloop over them. 
        print(event)   #prints out all the actions that take place on the screen
pygame.quit() #uninitialize the screen display
quit() #uninitialize everything









 
