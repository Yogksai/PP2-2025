import pygame
import os

image_library = {}
def get_image(path):
    global image_library
    image = image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        image_library[path] = image
    return image

pygame.init() #kicks things off. It initializes all the modules required for PyGame
screen = pygame.display.set_mode((1000, 1000)) #launch a window of the desired size
done = False
clock = pygame.time.Clock() #this is the function that creates a clock object. The clock object is used to control the frame rate of the game. It is used to limit the number of frames per second that the game will run at. The clock object is created with a default frame rate of 60 frames per second. This means that the game will run at 60 frames per second unless you change it.

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255,255,255))

    screen.blit(get_image('mickeyclock.jpeg'), (20, 20))

    pygame.display.flip()
    clock.tick(60)