import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((750,300))
screen.fill('white')
pygame.display.set_caption('game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('sus',False, 'red')

enemy_surface = pygame.image.load('graphics/Enemy1/Anim1.png').convert_alpha()
enemy_x_pos = 750

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,-100))
    screen.blit(ground_surface,(-1,200))
    screen.blit(text_surface,(300,50))
    enemy_x_pos -= 4
    if enemy_x_pos < -50:
         enemy_x_pos = 750
    
    screen.blit(enemy_surface,(enemy_x_pos,120))

    pygame.display.update()
    clock.tick(60)