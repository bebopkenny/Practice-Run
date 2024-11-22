import pygame
from player import *
from sys import exit # Importing for exiting the program

pygame.init() # Starts pygame and starts all features like sound

screen = pygame.display.set_mode((800, 400)) # Game width and height window
pygame.display.set_caption('Runner') # Changes title of the screen
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # Arguments are font type and font size

sky_image = pygame.image.load('pictures/Sky.png').convert_alpha() # Importing images
ground_image = pygame.image.load('pictures/Ground.png').convert_alpha()

score_surface = test_font.render('Score', False,(64, 64, 64))# Arguments are text info, alias, and color; Lets you costumize the text
score_rect = score_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('snail/snail1.png').convert_alpha() # convert_alpha helps imgs load faster
snail_x_pos = 600 # Declare a variable for the X position to move Left or Right
snail_rect = snail_surface.get_rect(bottomright = (snail_x_pos, 300))

player_surf = pygame.image.load('player/sonic_idle.png').convert_alpha() # Input surface of player
sonic_surf = pygame.transform.scale(player_surf, (128, 150))
player_rect = sonic_surf.get_rect(midbottom = (80, 312)) # Left, top, width, height
player_gravity = 0

# test_surface = pygame.Surface((100, 200)) # Display surface; It is always on
# test_surface.fill('Red') # Fills test_surface varible with color Red

# Loop to keep game running
while True:
    for event in pygame.event.get(): # Gets all of the events
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
            #player_rect.collidepoint(event.pos):
            #print('collision')
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE:
                print('jump')

        if event.type == pygame.KEYUP:
            print('key up')

    screen.blit(sky_image, (0, 0)) # Blit lets us place one surface onto the other; Uses X & Y
    screen.blit(ground_image, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect) # Call draw then what shape
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    # pygame.draw.ellipse(screen, (133, 84, 123), pygame.Rect(50, 200, 100, 100))

    screen.blit(score_surface, score_rect)
    # snail_x_pos -= 4 # Condition if snail goes too far to the left
    # if snail_x_pos < -100: 
        # snail_x_pos = 800
    snail_rect.x -= 4
    if snail_rect.right <= 0: 
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)

    # PLAYER 
    player_gravity += 1
    player_rect.y += player_gravity
    screen.blit(sonic_surf, player_rect)
    print(sonic_surf)

    if player_rect.colliderect(snail_rect): # First character then check if it collides with second character; No = 0 Yes = 1
        print('collision')
    
    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint(mouse_pos):
        #print(pygame.mouse.get_pressed())

    # draw all elements and updates everything
    pygame.display.update()
    clock.tick(60) # Frame rate