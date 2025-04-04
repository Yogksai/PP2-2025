import pygame

pygame.init() #kicks things off. It initializes all the modules required for PyGame
screen = pygame.display.set_mode((400, 300)) #launch a window of the desired size
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock() #this is the function that creates a clock object. The clock object is used to control the frame rate of the game. It is used to limit the number of frames per second that the game will run at. The clock object is created with a default frame rate of 60 frames per second. This means that the game will run at 60 frames per second unless you change it.

while not done:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        
        pressed = pygame.key.get_pressed() #this is the function that gets the state of all the keys. It returns a list of boolean values, one for each key. If the key is pressed, the value is True. If the key is not pressed, the value is False.
        if pressed[pygame.K_UP]: y -= 3 #this is the function that checks if the up arrow key is pressed
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3 #this is the function that checks if the left arrow key is pressed
        if pressed[pygame.K_RIGHT]: x += 3

        screen.fill((0,0,0))
        if is_blue: color = (0,128,255)
        else: color = (255,100,0)
        pygame.draw.rect(screen, color, pygame.Rect(x,y, 60, 60)) #this is the function that draws a rectangle on the screen. The first argument is the surface to draw on. The second argument is the color of the rectangle. The third argument is the rectangle to draw. The rectangle is defined by its top left corner and its width and height. The top left corner is defined by its x and y coordinates. The width and height are defined by their width and height in pixels.
        
        
        
        
        
        pygame.display.flip() #this is the function that updates the contents of the entire display. It is called every time through the loop, so it will be called 60 times a second if you are running at 60 frames per second. If you are running at 30 frames per second, it will be called 30 times a second. If you are running at 10 frames per second, it will be called 10 times a second. If you are running at 1 frame per second, it will be called 1 time a second. If you are running at 0 frames per second, it will not be called at all.
        clock.tick(60)