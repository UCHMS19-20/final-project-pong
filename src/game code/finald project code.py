
import pygame
from paddle import Paddle
 
pygame.init()
 

BLACK = (0,0,0)
WHITE = (255,255,255)
 

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
 
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200
 

all_sprites_list = pygame.sprite.Group()
 

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
 

play_verif = True
 

clock = pygame.time.Clock()
 

while play_verif:
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              play_verif = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     play_verif = False  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)     
                    
 
    all_sprites_list.update()
 
 
    
    
    screen.fill(BLACK)
   
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    
    all_sprites_list.draw(screen) 
 

    pygame.display.flip()
     
    
    clock.tick(60)
 

pygame.quit()