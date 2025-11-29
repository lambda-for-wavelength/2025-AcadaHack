#blah blah blah

import pygame 
import objects

pygame.init()

#Screen size in pixels 
Screen_Width = 320
Screen_Height = 320

#Makes a camera, Screen, and player
Screen = pygame.display.set_mode((Screen_Height, Screen_Height))
clock = pygame.time.Clock()
player = objects.Player(Screen_Width/2, Screen_Height/2)
Map = pygame.image.load("textures/Map test.png")
Map_rect = Map.get_rect()
dt = 0
#Wall = pygame.rect((200, 120, 32, 32))
#camera = 

crate_g = pygame.sprite.Group()
c = objects.Crate(64, 64)
crate_g.add(c)

wall_g = pygame.sprite.Group()
w = objects.Wall(128, 128)
wall_g.add(w)

groups = [crate_g, wall_g]
player.groups_list = groups

#this is the game loop
run = True
while run == True:

    #this referches and draws the screen
    Screen.fill((0, 0, 0))
    Screen.blit(player.image, player.rect)
    player.update(dt)
    crate_g.draw(Screen)
    crate_g.update(dt)
    wall_g.draw(Screen)
    wall_g.update(dt)

    #this is the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    dt = clock.tick(60)

#This is to end the game
pygame.quit()