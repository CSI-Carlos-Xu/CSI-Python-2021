import pygame #It calls the module where the game is.
pygame.init() #This step initialize the game.
dis=pygame.display.set_mode((400,300)) #This creates a display for the game with those dimensions.

blue=(0,0,255) #Establishing the colors with its RGB number. 
red=(255,0,0) #Establishing the colors with its RGB number. 
game_over=False #Here, a variable is created to define that the game_over equals false.
 

pygame.display.set_caption('Snake game by Carlos Xu') #This string names the screen. 


while not game_over: #This is a loop that will keep repeating itself until the gameover variable has been set to true. 
    for event in pygame.event.get(): #get every event as a list and run a forloop over them. 

        if event.type==pygame.QUIT: #Here, system receives an event which quits the game.
             game_over=True #If it receives a quit event, then the forloop ends.
    pygame.draw.rect(dis,blue,[200,150,10,10]) #Set the position (coordinates 200, 150- in the middle) and size (10, 10- pixels) of the snake.
    pygame.display.update() #This step updates the display of the screen.  
        
      
pygame.quit() #uninitialize the screen display
quit() #uninitialize everything



 

   
  








    
        
           
 




 
