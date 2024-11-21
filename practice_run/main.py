import pygame
from sys import exit # Importing for exiting the program

pygame.init() # Starts pygame and starts all features like sound

screen = pygame.display.set_mode((800, 400)) # Game width and height window
pygame.display.set_caption('Runner') # Changes title of the screen
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # Arguments are font type and font size

sky_image = pygame.image.load('pictures/Sky.png').convert_alpha() # Importing images
ground_image = pygame.image.load('pictures/Ground.png').convert_alpha()
text_surface = test_font.render('My game', False, 'Black') # Arguments are text info, alias, and color; Lets you costumize the text

snail_surface = pygame.image.load('snail/snail1.png').convert_alpha()
snail_x_pos = 600 # Declare a variable for the X position to move Left or Right

player_surf = pygame.image.load('pictures/')# Input surface of player

# test_surface = pygame.Surface((100, 200)) # Display surface; It is always on
# test_surface.fill('Red') # Fills test_surface varible with color Red

# Loop to keep game running
while True:
    for event in pygame.event.get(): # Gets all of the events
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

    screen.blit(sky_image, (0, 0)) # Blit lets us place one surface onto the other; Uses X & Y
    screen.blit(ground_image, (0, 300))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= 4
    if snail_x_pos < -100: 
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250))
    
    # draw all elements and updates everything
    pygame.display.update() 
    clock.tick(60) # Frame rate