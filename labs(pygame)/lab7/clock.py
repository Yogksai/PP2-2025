import pygame
from datetime import datetime

pygame.init()

mainclock = pygame.image.load('mainclock.png')
left_hand = pygame.image.load('leftarm.png')
right_hand = pygame.image.load('rightarm.png')

screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()

mainclock_rect = mainclock.get_rect(center=(450, 450))
left_hand_rect = left_hand.get_rect(center=mainclock_rect.center)
right_hand_rect = right_hand.get_rect(center=mainclock_rect.center)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = datetime.now().time()

    second_angle = current_time.second * 6
    minutes_angle = current_time.minute * 6 + current_time.second / 20

    rotate_left_hand = pygame.transform.rotate(left_hand, -second_angle)
    rotate_right_hand = pygame.transform.rotate(right_hand, -minutes_angle)

    left_hand_rect = rotate_left_hand.get_rect(center=mainclock_rect.center)
    right_hand_rect = rotate_right_hand.get_rect(center=mainclock_rect.center)

    screen.blit(mainclock, mainclock_rect)  
    screen.blit(rotate_left_hand, left_hand_rect) 
    screen.blit(rotate_right_hand, right_hand_rect) 

    pygame.display.update([left_hand_rect, right_hand_rect])

    clock.tick(60)