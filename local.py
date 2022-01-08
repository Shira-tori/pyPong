import pygame

pygame.font.init()

SCREEN_SIZE = 640, 480
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN)
myFont = pygame.font.Font("Silverfinster-x3L2K.ttf", 20)
Clock = pygame.time.Clock()

black = 0, 0, 0
white = 255, 255, 255

player1score = 0
player2score = 0
