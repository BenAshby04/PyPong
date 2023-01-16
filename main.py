import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))
gameloop = True

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    #Main Game loop to draw everything
    
    pygame.display.update()