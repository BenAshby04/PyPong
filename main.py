import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
gameloop = True
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

left_paddle = pygame.Surface((20,100))
left_paddle.fill(pygame.Color(255,255,255))
left_paddelX = 10
left_paddleY = 10


right_paddle = pygame.Surface((20,100))
right_paddle.fill(pygame.Color(255,255,255))
right_paddleX= 770
right_paddleY = 10


while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()   
    screen.fill(pygame.Color(0,0,0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddleY = left_paddleY - 2
    if keys[pygame.K_s]:
        left_paddleY = left_paddleY + 2
    if keys[pygame.K_UP]:
        right_paddleY = right_paddleY -2
    if keys[pygame.K_DOWN]:
        right_paddleY = right_paddleY + 2
            
    screen.blit(left_paddle,(left_paddelX,left_paddleY))
    screen.blit(right_paddle,(right_paddleX,right_paddleY))
    #Main Game loop to draw everything
    
    
    
    pygame.display.update()
    clock.tick(60)