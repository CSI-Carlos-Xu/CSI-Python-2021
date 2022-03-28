import pygame #It calls the module where the game is.
pygame.init() #This step initialize the game.
import time


blue=(0,0,255) #Establishing the colors with its RGB number. It is the snake's color
red=(255,0,0) #Establishing the colors with its RGB number. 
white = (255, 255, 255)
black = (0, 0, 0)

dis_width = 800 #Indicates the width of the display.
dis_height  = 600 ##Indicates the height of the display.

 
dis=pygame.display.set_mode((dis_width,dis_height)) #This creates a display for the game with those dimensions.
pygame.display.set_caption('Snake game by Carlos Xu') #This string names the screen. 

game_over=False #Here, a variable is created to define that the game_over equals false.

x1 = dis_width/2 #indicates the position of the snake in the display in terms of the x-axis. 
y1 = dis_height/2 #indicates the position of the snake in the display in terms of the y-axis. 

snake_block=10 #Dimensions of the snake. 

 
x1_change = 0  # This is to hold the updating values of the x and y coordinates.    
y1_change = 0  # This is to hold the updating values of the x and y coordinates.    

clock = pygame.time.Clock() #To see the time frame while the snake is moving. 
snake_speed=20 #Speed of the snake

font_style = pygame.font.SysFont(None, 50) #Indicates the font and size of the letters for game over message.  

def message(msg,color): #defining the message function.
    mesg = font_style.render(msg, True, color) #Indicates the three parameters for the game over message (the correct message and its color)
    dis.blit(mesg, [dis_width/3, dis_height/2]) #Indicates where the message is going to appear (its position)
 
 

while not game_over: #This is a loop that will keep repeating itself until the gameover variable has been set to true. 
    for event in pygame.event.get(): #get every event as a list and run a forloop over them. 

        if event.type==pygame.QUIT: #Here, system receives an event which quits the game.
             game_over=True #If it receives a quit event, then the forloop ends.

        if event.type == pygame.KEYDOWN: #Establishes the keyboard keys that are being used while playing the game. 
            if event.key == pygame.K_LEFT: #Indicates the use of the left arrow. 
                x1_change = -snake_block # When pressing it, the snake will move -10 in x-axis. 
                y1_change = 0 # When pressing it, the snake will not move in the y-axis. 
            elif event.key == pygame.K_RIGHT: #Indicates the use of the right arrow. 
                x1_change = snake_block # When pressing it, the snake will move 10 in x-axis. 
                y1_change = 0  # When pressing it, the snake will not move in the y-axis.
            elif event.key == pygame.K_UP: #Indicates the use of the upper arrow. 
                y1_change = -snake_block #When pressing it, the snake will move -10 in y-axis. 
                x1_change = 0 #When pressing it, the snake will not move in the x-axis.
            elif event.key == pygame.K_DOWN: #Indicates the use of the lower arrow. 
                y1_change = snake_block #When pressing it, the snake will move 10 in y-axis. 
                x1_change = 0 #When pressing it, the snake will not move in the x-axis.

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #If the snake touches the boundaries of the display, the game is over. 
        game_over = True #Game is over. 

    x1 += x1_change #Does an update of the snake position in the x-axis. 
    y1 += y1_change #Does an update of the snake position in the y-axis. 
    dis.fill(white) #Indicates that the display will be white. 

    pygame.draw.rect(dis,blue,[x1,y1,snake_block, snake_block]) #Set the position (coordinates 200, 150- in the middle) and size (10, 10- pixels) of the snake.
    pygame.display.update() #This step updates the display of the screen.  
        
 
    clock.tick(snake_speed) #Speed of the snake.

message("Game over!!!",red) #Calls the message function.
pygame.display.update() #Updates the display. 
time.sleep(2) #Creates a time limit for the message in the display. 

      
pygame.quit() #uninitialize the screen display
quit() #uninitialize everything




 

 
   
 


 




 



        
 

 

   
  








    
        
           
 




 
