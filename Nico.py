#blah blah blah

import pygame 
import time

pygame.init()

#Screen size in pixels 
Screen_Width = 320
Screen_Height = 320

#Makes a camera, Screen, and player
Screen = pygame.display.set_mode((Screen_Height, Screen_Height))
player = pygame.Rect((80, 72, 32, 32))
Map = pygame.image.load('data', 'bla.png')
#Wall = pygame.rect((200, 120, 32, 32))
#camera = 

#this is the game loop
run = True
while run == True:
    print(player)
    #this referches and draws the screen
    Screen.fill((0, 0, 0))
    pygame.draw.rect(Screen, (255, 255, 255), player)

    #checks for moverment
    time.sleep(0.08) 
    Key = pygame.key.get_pressed()
    if Key[pygame.K_w] == True:
        player.move_ip(0, -32)
    elif Key[pygame.K_a] == True:
        player.move_ip(-32, 0)
    elif Key[pygame.K_s] == True:
        player.move_ip(0, +32)
    elif Key[pygame.K_d] == True:
        player.move_ip(+32, 0)
    

    #this is the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

#This is to end the game
pygame.quit()