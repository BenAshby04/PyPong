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

lpadle = pygame.Rect(left_paddelX,left_paddleY,20,100)


right_paddle = pygame.Surface((20,100))
right_paddle.fill(pygame.Color(255,255,255))
right_paddleX= 770
right_paddleY = 10
rpadle = pygame.Rect(right_paddleX,right_paddleY,20,100)

# ball = pygame.Surface((20,20))
# ball.fill(pygame.Color(255,255,255))

ballX = 390
ballY = 190
ballVel = 5
ballUp=1
ballRight=1
ball = pygame.Rect(ballX,ballY,20,20)


while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()   
    screen.fill(pygame.Color(0,0,0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if left_paddleY > 0:
            left_paddleY = left_paddleY - 2
    if keys[pygame.K_s]:
        if left_paddleY < 300:
            left_paddleY = left_paddleY + 2
    if keys[pygame.K_UP]:
        if right_paddleY > 0:
            right_paddleY = right_paddleY -2
    if keys[pygame.K_DOWN]:
        if right_paddleY < 300:
            right_paddleY = right_paddleY + 2 
    
    # screen.blit(left_paddle,(left_paddelX,left_paddleY))
    ball = pygame.Rect(ballX,ballY,20,20)
    lpadle = pygame.Rect(left_paddelX,left_paddleY,20,100)
    rpadle = pygame.Rect(right_paddleX,right_paddleY,20,100)
    pygame.draw.rect(screen,(255,255,255),lpadle)
    pygame.draw.rect(screen,(255,255,255),rpadle)
    pygame.draw.rect(screen,(255,255,255),ball)
    # screen.blit(right_paddle,(right_paddleX,right_paddleY))
    #Main Game loop to draw everything
    
    
    
    pygame.display.flip()
    clock.tick(120)