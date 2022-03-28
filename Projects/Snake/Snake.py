import pygame #It calls the module where the game is.
pygame.init() #This step initialize the game.


blue=(0,0,255) #Establishing the colors with its RGB number. It is the snake's color
red=(255,0,0) #Establishing the colors with its RGB number. 
white = (255, 255, 255)
black = (0, 0, 0)

 
dis=pygame.display.set_mode((800,600)) #This creates a display for the game with those dimensions.
pygame.display.set_caption('Snake game by Carlos Xu') #This string names the screen. 

game_over=False #Here, a variable is created to define that the game_over equals false.

x1 = 400 #indicates the position of the snake in the display in terms of the x-axis. 
y1 = 300 #indicates the position of the snake in the display in terms of the y-axis. 
 
x1_change = 0  # This is to hold the updating values of the x and y coordinates.    
y1_change = 0  # This is to hold the updating values of the x and y coordinates.    

clock = pygame.time.Clock() #To see the time frame while the snake is moving. 
 

while not game_over: #This is a loop that will keep repeating itself until the gameover variable has been set to true. 
    for event in pygame.event.get(): #get every event as a list and run a forloop over them. 

        if event.type==pygame.QUIT: #Here, system receives an event which quits the game.
             game_over=True #If it receives a quit event, then the forloop ends.

        if event.type == pygame.KEYDOWN: #Establishes the keyboard keys that are being used while playing the game. 
            if event.key == pygame.K_LEFT: #Indicates the use of the left arrow. 
                x1_change = -10 # When pressing it, the snake will move -10 in x-axis. 
                y1_change = 0 # When pressing it, the snake will not move in the y-axis. 
            elif event.key == pygame.K_RIGHT: #Indicates the use of the right arrow. 
                x1_change = 10 # When pressing it, the snake will move 10 in x-axis. 
                y1_change = 0  # When pressing it, the snake will not move in the y-axis.
            elif event.key == pygame.K_UP: #Indicates the use of the upper arrow. 
                y1_change = -10 #When pressing it, the snake will move -10 in y-axis. 
                x1_change = 0 #When pressing it, the snake will not move in the x-axis.
            elif event.key == pygame.K_DOWN: #Indicates the use of the lower arrow. 
                y1_change = 10 #When pressing it, the snake will move 10 in y-axis. 
                x1_change = 0 #When pressing it, the snake will not move in the x-axis.

    x1 += x1_change #Does an update of the snake position in the x-axis. 
    y1 += y1_change #Does an update of the snake position in the y-axis. 
    dis.fill(white) #Indicates that the display will be white. 

    pygame.draw.rect(dis,blue,[x1,y1,10,10]) #Set the position (coordinates 200, 150- in the middle) and size (10, 10- pixels) of the snake.
    pygame.display.update() #This step updates the display of the screen.  
        
 
    clock.tick(20) #Speed of the snake.

      
pygame.quit() #uninitialize the screen display
quit() #uninitialize everything




 



        
 

 

   
  








    
        
           
 




 
