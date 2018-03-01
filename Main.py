import pygame, sys,time
from pygame.locals import *

pygame.init()
pygame.font.init()
pygame.display.set_caption("Too Much Memory")
SCREENWIDTH = 800
SCREENHEIGHT = 800
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)

WHITE = (240, 240, 240)
pygame.mixer.music.load('HarvestMoonTheme.wav')
pygame.mixer.music.play(-1, 0.0)
# print(pygame.mixer.music.get_volume())
pygame.mixer.music.set_volume(0.55)

windowSurface = pygame.display.set_mode(SCREENSIZE)

while True:
    for event in pygame.event.get():
        #print(event)
        x, y = pygame.mouse.get_pos()

        if event.type == QUIT:  # or (x > 650 and x < 755 and y > 650 and y < 700):
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            soundObj = pygame.mixer.Sound('Click.wav')
            soundObj.play()
            time.sleep(1)
            soundObj.stop()

            if 469 < x < 620 and 498 < y < 600:
                pygame.quit()
                sys.exit()
            elif 178 < x < 380 and 498 < y < 600:
                pygame.quit()
                from TooMuchMemory import main

    windowSurface.fill(WHITE)
    if pygame.font:
        font = pygame.font.Font(None, 100)
        text = font.render("Too Much Memory", 1, (0, 0, 160))
        textpos = text.get_rect(x=100, y=280)
        windowSurface.blit(text, textpos)

    pygame.draw.rect(windowSurface, (0, 220, 0), (180, 500, 150, 100))  # x+40 y+35
    font3 = pygame.font.Font(None, 42)
    text3 = font3.render("Start", 0, (255, 255, 255))
    textpos3 = text3.get_rect(x=220, y=535)
    windowSurface.blit(text3, textpos3)

    pygame.draw.rect(windowSurface, (255, 0, 0), (470, 500, 150, 100))
    font2 = pygame.font.Font(None, 42)
    text2 = font2.render("Exit", 0, (255, 255, 255))
    textpos2 = text2.get_rect(x=520, y=535)
    windowSurface.blit(text2, textpos2)
    pygame.display.update()
