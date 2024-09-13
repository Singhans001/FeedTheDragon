import pygame

#Start pyagame modules
pygame.init()

#Set the display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode ((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display .set_caption("Feed The Dragon")

''' We will write more code here '''

#The main game loop
running= True
while running:
    for event in pygame. event. get ():
        if event. type == pygame.QUIT:
            running = False

pygame.quit()