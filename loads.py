import pygame

pygame.mixer.init()
pygame.font.init()
# logos
mun_logo = pygame.image.load('assets/MUN Logo.png')

# backgrounds
outside_engineering = pygame.image.load('assets/backgrounds/MUN Engineering Building Outside.jpg')
engineering_lobby = pygame.image.load('assets/backgrounds/engineering_lobby.jpg')
bruneau = pygame.image.load('assets/backgrounds/Bruneau Center Inside.jpg')
chem_lab = pygame.image.load('assets/backgrounds/Chemistry Lab.jpg')
old_sci_hall = pygame.image.load('assets/backgrounds/Old Science Lecture Hall.jpg')
outside_university_center = pygame.image.load('assets/backgrounds/outside_university_center.jpg')
eo_center = pygame.image.load('assets/backgrounds/eo_success.jpg')

current_background = outside_engineering

# music and sounds
pygame.mixer.music.load('assets/sounds/Wii Sports Resort (Remix).wav')
pygame.mixer.music.set_volume(0.25)
startup_sound = pygame.mixer.Sound('assets/sounds/NINTENDO Mii THEME (TRAP REMIX) - VANDER.wav')
lose_sound = pygame.mixer.Sound('assets/sounds/GTA Lose.wav')
boss_music = pygame.mixer.Sound('assets/sounds/Swordplay Showdown - Wii Sports Resort OST.wav')


# Sprites
newfoundland_coin = pygame.image.load('assets/Newfoundland Coin.png')
fail_img = pygame.image.load('assets/fail.png')
