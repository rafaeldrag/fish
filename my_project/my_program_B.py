#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 0. Import libraries
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('../')
import pygame 
import sys
from my_library import fish

# 1. Initailise the pygame library
pygame.init()

# 2. Variables
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# 3. Launch a game window
window = pygame.display.set_mode((600, 400))


# 4. Set up the main game loop
while True:
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()  
        
#    elif event.type == pygame.MOUSEBUTTONDOWN:
#        print("User pressed a mouse button")


    # 5. Draw
    window.fill(blue)
    fish(window,red)
    
    # 6. Update display
    pygame.display.update()
    
    # 7. Frame rate
    clock = pygame.time.Clock().tick(60)
