import pygame

pygame.init() #kicks things off. It initializes all the modules required for PyGame
screen = pygame.display.set_mode((400, 300)) #launch a window of the desired size
done = False

while not done:
        for event in pygame.event.get(): #this empties the event queue, Если вы этого не сделаете, сообщения Windows начнут накапливаться, и, по мнению операционной системы, ваша игра перестанет отвечать на запросы
                if event.type == pygame.QUIT: #This is the event type that is fired when you click on the close button in the corner of the window
                        done = True
        
        pygame.display.flip()

