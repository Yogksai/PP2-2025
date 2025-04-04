import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300)) #launch a window of the desired size

songs = ["/Users/kadera/PP2/lab7/lab7/Nirvana - Smells Like Teen Spirit .mp3", "/Users/kadera/PP2/lab7/lab7/Nirvana - Come As You Are .mp3"]
current_song = 0

pygame.mixer.music.load(songs[current_song])
pygame.mixer.music.play()
music_playing = True
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if music_playing:
                    pygame.mixer.music.pause()
                    music_playing = False
                else:
                    pygame.mixer.music.unpause()
                    music_playing = True
            elif event.key == pygame.K_RIGHT:
                current_song += 1
                if current_song >= len(songs):
                    current_song = 0
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_song -= 1
                if current_song < 0:
                    current_song = len(songs) -1
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()

    pygame.display.flip()
    