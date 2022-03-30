import pygame

pygame.mixer.init()
pygame.font.init()
# logos
mun_logo = pygame.image.load('assets/MUN Logo.png')

# backgrounds
outside_engineering = pygame.image.load('assets/MUN Engineering Building Outside.jpg')

current_background = outside_engineering

# music and sounds
pygame.mixer.music.load('assets/Wii Sports Resort (Remix).wav')
startup_sound = pygame.mixer.Sound('assets/NINTENDO Mii THEME (TRAP REMIX) - VANDER.wav')


# Sprites
newfoundland_coin = pygame.image.load('assets/Newfoundland Coin.png')
fail_img = pygame.image.load('assets/fail.png')
