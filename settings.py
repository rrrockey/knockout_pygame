import pygame, os, sys, math

# defining some basic colors
black = 0, 0, 0
white = 255, 255, 255
grey = 180, 180, 180
blue = 0, 0, 255
water_blue = 163, 226, 230
button_blue = 52, 155, 235

screen_width = 800
screen_height = 800
screen_size = screen_width, screen_height

# setting display
screen = pygame.display.set_mode(screen_size)
# creating clock object
clock = pygame.time.Clock()

# setting the fps limit
fps_limit = 60

# three states of the game
PHASE_PLAYER1_SETUP = 1
PHASE_PLAYER2_SETUP = 2
PHASE_SIMULATION = 3

