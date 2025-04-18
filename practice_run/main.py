# 1: 50
import pygame
from player import *
from random import randint
from sys import exit # Importing for exiting the program

def display_score():
    current_time = round((pygame.time.get_ticks() / 1000 - start_time))
    score_surface = test_font.render(f"Score:{current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list: 
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(buzzer_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

pygame.init() # Starts pygame and starts all features like sound

screen = pygame.display.set_mode((800, 400)) # Game width and height window
pygame.display.set_caption('Runner') # Changes title of the screen
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # Arguments are font type and font size
game_active = True
start_time = 0
score = 0

sky_image = pygame.image.load('pictures/Sky.png').convert_alpha() # Importing images
ground_image = pygame.image.load('pictures/Ground.png').convert_alpha()

#score_surface = test_font.render('Score', False,(64, 64, 64))# Arguments are text info, alias, and color; Lets you costumize the text
#score_rect = score_surface.get_rect(center = (400, 50))

# Obstacles
snail_surface = pygame.image.load('snail/snail1.png').convert_alpha() # convert_alpha helps imgs load faster
snail_x_pos = 600 # Declare a variable for the X position to move Left or Right
snail_rect = snail_surface.get_rect(bottomright = (snail_x_pos, 300)) # DO NOT NEED

buzzer_surface = pygame.image.load('snail/buzzer.png').convert_alpha()

obstacle_rect_list = []

player_surf = pygame.image.load('player/sonic_idle.png').convert_alpha() # Input surface of player
sonic_surf = pygame.transform.scale(player_surf, (128, 150))
player_rect = sonic_surf.get_rect(midbottom = (80, 312)) # Left, top, width, height
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('player/SXSG_Sonic.png').convert_alpha()
player_transform = pygame.transform.scale(player_stand, (350, 400))
player_stand_rect = player_transform.get_rect(center = (400, 200))

game_title_surface = test_font.render('Gotta Go Fast!', False, (111, 196, 169))
game_title_rec = game_title_surface.get_rect(center = (400, 130))

game_instructions_surface = test_font.render('Jump over snail', False, (111, 196, 169))
game_instructions_rec = game_instructions_surface.get_rect(midbottom = (400, 320))
# test_surface = pygame.Surface((100, 200)) # Display surface; It is always on
# test_surface.fill('Red') # Fills test_surface varible with color Red

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# Loop to keep game running
while True:
    for event in pygame.event.get(): # Gets all of the events
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYUP:
                if event.type == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = round((pygame.time.get_ticks() / 1000 - start_time))
        
        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(buzzer_surface.get_rect(bottomright = (randint(900, 1100), 210)))

    if game_active:
        screen.blit(sky_image, (0, 0)) # Blit lets us place one surface onto the other; Uses X & Y
        screen.blit(ground_image, (0, 300))
        #pygame.draw.rect(screen, '#c0e8ec', score_rect) # Call draw then what shape
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # pygame.draw.ellipse(screen, (133, 84, 123), pygame.Rect(50, 200, 100, 100))
        score = display_score()
        #screen.blit(score_surface, score_rect)
        # snail_x_pos -= 4 # Condition if snail goes too far to the left
        # if snail_x_pos < -100: 
            # snail_x_pos = 800
        #snail_rect.x -= 4
        #if snail_rect.right <= 0: 
            #snail_rect.left = 800
        #screen.blit(snail_surface, snail_rect)

        # PLAYER 
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: # If player goes below 300 then it will stay at 300
            player_rect.bottom = 300
        screen.blit(sonic_surf, player_rect)

        if player_rect.colliderect(snail_rect): # First character then check if it collides with second character; No = 0 Yes = 1
            print('collision')

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)   

        # Collision
        #if snail_rect.colliderect(player_rect):
            #game_active = False
        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill((94, 129, 164))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear() # Game resets
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_message_rec = score_message.get_rect(center = (400, 330))
        screen.blit(game_title_surface, game_title_rec)
        if score == 0:
            screen.blit(game_instructions_surface, game_instructions_rec)
        else:
            screen.blit(score_message, score_message_rec)

    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint(mouse_pos):
        #print(pygame.mouse.get_pressed())

    # draw all elements and updates everything
    pygame.display.update()
    clock.tick(60) # Frame rate